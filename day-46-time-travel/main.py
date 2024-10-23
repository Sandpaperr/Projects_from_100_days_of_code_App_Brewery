from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
import os

load_dotenv()

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

date = input("Which Year would you like to travel to? YYYY-MM-DD: ")

#TODO: Make sanity checks on the input

url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

titles_raw = soup.select("div ul li ul li h3")
artists_raw = soup.select("div ul li ul li span.c-label.a-no-trucate.a-font-primary-s")

titles = [raw.get_text().strip() for raw in titles_raw]
artists = [raw.get_text().strip() for raw in artists_raw]

#Spotipy
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

spotipy_object = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=" http://example.com")
#todo the rest

