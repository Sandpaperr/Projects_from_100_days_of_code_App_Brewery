from bs4 import BeautifulSoup
import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

date = input("Which Year would you like to travel to? YYYY-MM-DD: ")

#TODO: Make sanity checks on the input

url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
