from bs4 import BeautifulSoup, Tag
from typing import List
from dotenv import load_dotenv
import os
import requests


load_dotenv()



FORM = os.getenv("GOOGLE_FORM")

URL = "https://appbrewery.github.io/Zillow-Clone/"

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


all_links = []
all_prices = []
all_addresses = []

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

# The following sectioln needs to be adapted to the website we are using
all_listing = soup.find_all(class_="StyledCard-c11n-8-84") #type: List[Tag]

for house in all_listing:
    link = house.find("a").get("href")
    address = house.find("address").text.strip().replace("|", "").replace("\n","")
    price = house.find(class_="PropertyCardWrapper__StyledPriceLine").text[:-3].split("+")[0]


    #TODO: handle error when a is not found
    #TODO: clean text before submitting it 
    all_links.append(link)
    all_addresses.append(address)
    all_prices.append(price)



print(len(all_links))
print(len(all_addresses))
print(all_prices)


