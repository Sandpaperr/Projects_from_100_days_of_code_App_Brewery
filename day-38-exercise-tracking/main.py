import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


#TODO: problem with authentication. Probably the tokens have expired

# Exercise api
APP_ID = os.getenv("EXERCISE_APP_ID")
API_KEY = os.getenv("EXERCISE_API_KEY")
EXERCISES_ENDPOINT = os.getenv("EXERCISE_ENDPOINT")

# Info
GENDER = "male"
WEIGHT_KG = "86"
HEIGHT_CM = "183"
AGE = "22"

# Sheety api
WORKOUT_SHEET_ENDPOINT = os.getenv("WORKOUT_SHEET_ENDPOINT")
Token = os.getenv("SHEETY_TOKEN")



# START PROGRAM ======================================
plain_text = input("Tell me which exercises you did: ")

# Exercise ------------------------------------
exercise_params = {
    "query":plain_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# translate plain text in information
response = requests.post(EXERCISES_ENDPOINT, headers=headers, json=exercise_params)
print(response.text)
# -----------------------------------------------------

# Sheet ----------------------------------------
data = response.json()

for i in range(0, len(data["exercises"])):

    today_date = datetime.today().strftime("%d/%m/%Y")
    time_now = datetime.now().strftime("%H:%M:%S")
    data_exercise= data["exercises"][i]["name"]
    data_duration = round(data["exercises"][i]["duration_min"])
    data_calories = round(data["exercises"][i]["nf_calories"])


    playload_sheet = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": data_exercise,
            "duration": data_duration,
            "calories": data_calories,
        }
    }

    header_sheet = {
        "Authorization": "Bearer Ambarabaciccicocco##"
    }

    print(playload_sheet)
    response = requests.post(url=WORKOUT_SHEET_ENDPOINT, json=playload_sheet, headers=header_sheet)
    print(response.text)
    # -----------------------------------------------------