import requests
import os
from datetime import datetime

from dotenv import load_dotenv

# Load env variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6bc3c104079e0d72c3eae6ad72f60ca5/workoutTracking/workout"

query = "I ran 5 mile"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": query,
    "gender": "Male",
    "weight_kg": 80,
    "height_cm": 186,
    "age": 24
}

response = requests.post(url=exercise_endpoint,
                         json=params,
                         headers=headers)

response.raise_for_status()

result = response.json()

sheety_headers = {
    "Authorization": f'Bearer {SHEETY_TOKEN}'
}

for exercise in result["exercises"]:
    date = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%X")

    # post a new row
    post_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheet_endpoint,
                                   headers=sheety_headers,
                                   json=post_params)

    sheet_response.raise_for_status()

    print(sheet_response.text)
