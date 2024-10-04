import requests
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_KEY = os.getenv("TEQUILA_KIWI_API_KEY")
        self.header = {"apikey": self.API_KEY}
        self.url = "https://api.tequila.kiwi.com"

    def get_iata(self, city_name: str):
        print(city_name)
        location_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
        }
        url_get_location = f"{self.url}/locations/query"
        iata_response = requests.get(url=url_get_location, params=location_params, headers=self.header)
        data = iata_response.json()
        city_iata = data["locations"][0]["city"]["code"]
        print(city_iata)
        return city_iata

    def flight_check(self, origin_iata: str, destination_iata: str, from_time, to_time):
        url_search = f"{self.url}/v2/search"
        params_search_flight = {
            "fly_from": origin_iata,
            "fly_to": destination_iata,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to ": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 15,
            "flight_type": "round",
            "adults": 1,
            "adult_hold_bag": 0,
            "adult_hand_bag": 0,
            "curr": "GBP",
            "limit": 4,
            "max_stopovers": 0,
            "max_fly_duration": 5,


        }
        search_response = requests.get(url=url_search, params=params_search_flight, headers=self.header)
        search_response.raise_for_status()
        try:
            data = search_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_iata}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data


