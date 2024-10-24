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

song_names = [raw.get_text().strip() for raw in titles_raw]
artists = [raw.get_text().strip() for raw in artists_raw]

#Spotipy
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIFY_USERNAME = os.getenv("SPOTIFY_USERNAME")

sp_oauth = spotipy.oauth2.SpotifyOAuth(
                                 client_id=CLIENT_ID, 
                                 client_secret=CLIENT_SECRET, 
                                 redirect_uri="http://localhost:8080/spotify/callback", 
                                 scope='playlist-modify-private',
                                 show_dialog=True,
                                 cache_path=r"day-46-time-travel\token.txt",
                                 )

# Fetch the token, prefer using `get_cached_token()` if available
token_info = sp_oauth.get_cached_token()

# If the token is not cached, get a new token
if not token_info:
    token_info = sp_oauth.get_access_token(as_dict=False)

# Now use the token to authenticate with Spotipy
if token_info:
    sp = spotipy.Spotify(auth=token_info['access_token'])

    # Fetch the current user information
    try:
        user_info = sp.current_user()
        user_id = user_info["id"]
        print(f"Your Spotify User ID is: {user_id}")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error fetching user information: {e}")
else:
    print("Failed to retrieve access token.")


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)