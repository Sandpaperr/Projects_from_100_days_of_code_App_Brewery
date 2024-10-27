from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
PASSWORD = os.getenv("PASSWORD")

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
  }



#Static URL for amazon
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=url, headers=header)

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
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )