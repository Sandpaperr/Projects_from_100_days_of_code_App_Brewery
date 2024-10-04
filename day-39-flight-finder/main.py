# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

from data_manager import  DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "MAN" # Manchester

#TODO: something has changed with the API, double check.
data = data_manager.get_data()

pprint(data)

for city in data:
    # Fill IATAs
    if not city["iataCode"]:
        city_iata = flight_search.get_iata(city["city"])
        row_id = city["id"]
        data_manager.update_iata(city_iata, row_id)

    # Check for flights
    tomorrow = datetime.now() + timedelta(days=15)
    six_months_from_today = datetime.now() + timedelta(days=(6 * 30))
    flight = flight_search.flight_check(origin_iata=ORIGIN_CITY_IATA, destination_iata=city["iataCode"],
                                        from_time=tomorrow, to_time=six_months_from_today)

    try:
        if flight.price < city["lowestPrice"]:
            NotificationManager().send_notification(flight)
        else:
            print("flight price is not lower than the set price")

    except AttributeError:
        continue
