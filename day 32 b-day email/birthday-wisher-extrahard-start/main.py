##################### Extra Hard Starting Project ######################


import pandas as p
from random import randint
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"./day 32 b-day email\.env")


my_email = os.getenv("EMAIL")
two_step = os.getenv("TWO_STEP")

# 1. Update the birthdays.csv
with open(r"./day 32 b-day email\birthday-wisher-extrahard-start\birthdays.csv", "r") as file:
    row_data = p.read_csv(file)
    data_dictionary = row_data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for person in data_dictionary:

    # 2. Check if today matches a birthday in the birthdays.csv
    if person["month"] == month and person["day"] == day:

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        file_name = f"./letter_templates/letter_{randint(1, 3)}.txt"
        with open(file_name, "r") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", person["name"], 1)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=two_step)
            connection.sendmail(
                from_addr=my_email, to_addrs=person["email"],
                msg=f"Subject:Happy birthday {person['name']}\n\n {letter}"
            )
