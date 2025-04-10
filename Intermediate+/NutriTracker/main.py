import requests
import os
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

AGE = 27
WEIGHT = 75

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("What did you do? "),
    "weight_kg": WEIGHT,
    "age": AGE
}

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url= api_endpoint, json= parameters, headers= headers)
response.raise_for_status()
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

for exercise in result["exercises"]:
    upload_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url= SHEET_ENDPOINT, json= upload_params, headers= sheety_header)
    print(response.text)