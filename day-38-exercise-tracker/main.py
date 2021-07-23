import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
TOKEN = ""

GENDER = "female"
WEIGHT_KG = None  # Update with actual weight
HEIGHT_CM = None  # Update with actual height
AGE = 21

today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%H:%M:%S")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = ""

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercise_data = exercise_response.json()

for exercise in exercise_data['exercises']:
    exercise_name = exercise['name'].title()
    exercise_duration = round(exercise['duration_min'])
    calories_burned = round(exercise['nf_calories'])

    sheety_params = {
        "workout": {
              "date": formatted_date,
              "time": formatted_time,
              "exercise": exercise_name,
              "duration": exercise_duration,
              "calories": calories_burned
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=bearer_headers)
    print(sheety_response.text)
