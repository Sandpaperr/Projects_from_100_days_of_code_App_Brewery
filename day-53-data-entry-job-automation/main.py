import time
from bs4 import BeautifulSoup, Tag
from typing import List
from dotenv import load_dotenv
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException


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




def scrape_addresses_links_prices_from_Zillow_static():

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
    return all_addresses, all_links, all_prices


def fill_all_google_form(addresses:list, links:list, prices:list):
    if len(addresses) == len(links) == len(prices):

        #Init selenium driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(FORM)


        for i in range(len(addresses)):
            #I am thinking of placing the find element outside of the loop. Does the element change when refreshing?
            input_address = driver.find_element(By.XPATH, value=r'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_price = driver.find_element(By.XPATH, value=r'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            input_link = driver.find_element(By.XPATH, value=r'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = driver.find_element(By.XPATH, value=r'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

            input_address.send_keys(addresses[i])
            input_price.send_keys(prices[i])
            input_link.send_keys(links[i])
            submit_button.click()
            time.sleep(1)
            another_response_link = driver.find_element(By.XPATH, value=r'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_response_link.click()
            time.sleep(1)
            print()
            print()
            print(addresses[i])
            print(prices[i])
            print(links[i])
            print("Submitted properly")


        
    else:
        print("given lists contain uneven number of elements")





scraped_addresses, scraped_links, scraped_prices = scrape_addresses_links_prices_from_Zillow_static()
fill_all_google_form(scraped_addresses, scraped_links, scraped_prices)

