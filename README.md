# Workout log

## Description

Workout log is a Python script that lets you log your workout using natural language. The script uses the Nutritionix API for natural language processing and the Sheety project for storing user data.


## Installation & Configuration

As with most other Python applications, this script also requires the installation of necessary dependencies. You can install them using pip:
```
pip install -r requirements.txt
```

To make the script work, you need to set up your own project on [Sheety](https://sheety.co/) using your own copy of [this template](https://docs.google.com/spreadsheets/d/14folwte3oSKwOz8OuUnaPid56bvhQNoxgG7jtudf_iY/edit?usp=sharing).
On the Authentication tab, choose the type 'Bearer (Token)'.

You also need a Nutrition APP ID and API KEY which you can obtain [here](https://developer.nutritionix.com/).

Place the resulting data in an `.env` file in the script folder as follows

```
NUTRITIONIX_APP_ID=<Your nutrutionix App ID>
NUTRITIONIX_API_KEY=<Your nutrutionix API KEY>
WORKOUT_TOKEN=<Your workout sheet Token>

```


## Usage 

When run, the script asks the user for input:
```
What exercise you did:
```

You can write completed exercises in natural language, e.g.,
```
What exercise you did: I did 50 minutes of running and then I cycled for 1 hour.
```

This results in new logs in a Google spreadsheet:


| Date       | Time     | Exercise     | Duration | Calories |
|------------|----------|--------------|----------|----------|
| 17/10/2024 | 18:24:46 | Running      |       50 |   669.67 |
| 17/10/2024 | 18:24:47 | Road cycling |       60 |      820 |
