import time

import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"./day 32 b-day email\.env")


my_email = os.getenv("EMAIL")
two_step = os.getenv("TWO_STEP")

MY_LATITUDE = 53.807149
MY_LONGITUDE = -1.552325




def iss_is_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # My position is within +5 or -5 degrees of the ISS position

    # and if the ISS is close to my current position
    if iss_latitude - 5 <= MY_LATITUDE <= iss_latitude + 5 and iss_longitude - 5 < MY_LONGITUDE < iss_longitude + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_row = data["results"]["sunrise"]
    sunset_row = data["results"]["sunset"]

    sunrise_hour = int(sunrise_row.split("T")[1].split(":")[0])
    sunset_hour = int(sunset_row.split("T")[1].split(":")[0])
    current_hour = datetime.now().hour

    # if it's night
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True

while True:
    # Then send me an email to tell me to look up
    if is_night() and iss_is_overhead():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=two_step)
            connection.sendmail(
                from_addr=my_email, to_addrs="russo.leand@gmail.com",
                msg=f"Subject: LOOK UP\n\n Hurry up\nLook at the sky, the ISS is close and beautiful"
            )
    # BONUS: run the code every 60 seconds
    time.sleep(60)

