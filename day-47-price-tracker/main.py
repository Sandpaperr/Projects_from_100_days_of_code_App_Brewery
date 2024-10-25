from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
SMTP_ADDRESS = ""
PASSWORD = ""


#Static URL for amazon
url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=url)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="a-price-whole").get_text()
price = float(price + soup.find(class_="a-price-fraction").get_text()) 


print(price)

# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )