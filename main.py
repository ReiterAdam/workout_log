import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
WORKOUT_TOKEN = os.getenv('WORKOUT_TOKEN')
USER_KG = 82
USER_CM = 188
USER_AGE = 27

def main():
    user_input = input('What exercise you did: ')

    # send user input to nutritionix
    response = send_request(user_input)

    # scope data from response for exercise
    rows = prepare_rows(response)

    # post row(s) with scoped data
    for row in rows:
        add_row_to_workouts(row)


def send_request(user_input):

    nut_domain = 'https://trackapi.nutritionix.com'
    exercise_endpoint = f'{nut_domain}/v2/natural/exercise'

    header = {
        'Content-Type': 'application/json',
        'x-app-id': NUTRITIONIX_APP_ID,
        'x-app-key': NUTRITIONIX_API_KEY
    }
    
    parameters = {
        'query': user_input,
        'weight_kg': USER_KG,
        'height_cm': USER_CM,
        'age': USER_AGE 
    }

    response = requests.post(
        url=exercise_endpoint,
        headers=header,
        json=parameters
    )

    data = response.json()
    response.raise_for_status()
    return data


def add_row_to_workouts(row):
    url = 'https://api.sheety.co/14bb820ea18375ca7fafaf94629b2ff5/myWorkouts/workouts'

    header = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {WORKOUT_TOKEN}"
    }

    now = dt.datetime.now()

    body = {
        'workout': {
            'date': now.strftime("%d/%m/%Y"),
            'time': now.strftime("%H:%M:%S"),
            'exercise': row['exercise'].capitalize(),
            'duration': row['duration'],
            'calories': row['calories']
        }
    }

    response = requests.post(
        url=url,
        headers=header,
        json=body
    )

    data = response.json()
    response.raise_for_status()
    return data


def prepare_rows(response):
    rows = []
    for exercise in response['exercises']:
        row = {
            'exercise': exercise['name'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
        rows.append(row)
    return rows


if __name__ == '__main__':
    main()