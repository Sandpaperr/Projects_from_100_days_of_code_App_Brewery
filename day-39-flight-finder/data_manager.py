import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Exercise api
        self.token = os.getenv("SHEETY_TOKEN")
        self.url_for_get = "https://api.sheety.co/587168505238b986fd972eb989af2049/flightDealsProject/prices"
        self.headers = {"Authorization": self.token}

    def get_data(self):
        response = requests.get(self.url_for_get, headers=self.headers)
        return response.json()

    def update_iata(self, city_iata: str, row_id: int):
        url_for_put = f"https://api.sheety.co/587168505238b986fd972eb989af2049/flightDealsProject/prices/{row_id}"
        body = {
            "price": {
                "iataCode": city_iata,
            }
        }
        response_put = requests.put(url_for_put, json=body, headers=self.headers)
