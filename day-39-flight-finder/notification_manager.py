from twilio.rest import Client
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("NEWS_ACCOUNT_SID")
        self.auth_token = os.getenv("NEWS_AUTH_TOKEN")

    def send_notification(self, flight: FlightData):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"\nLow price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                 f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}",
            from_="+18788880816",
            to="+447742200038"
        )
        print(message.status)

