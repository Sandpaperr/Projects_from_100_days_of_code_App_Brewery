import smtplib
import datetime as dt
from random import randint
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"./day 32 b-day email\.env")

my_email = os.getenv("EMAIL")
two_step = os.getenv("TWO_STEP")



now = dt.datetime.now()
day = now.weekday()

if day == 0:
    with open(r"./day 32 b-day email\motivational quotes\quotes.txt", "r") as file:
        quotes = file.readlines()
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=two_step)
            connection.sendmail(
                from_addr=my_email, to_addrs="trypython@yahoo.com",
                msg=f"Subject:Hello\n\n {quotes[randint(0, len(quotes) - 1)]}"
            )
