import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

#TODO: can't authenticate anymore, probably the twilio account has expired. Make a new one
api_key = os.getenv("TWILIO_API")
MY_LATITUDE = 47.8095#53.807149
MY_LONGITUDE = 13.0550#-1.552325
account_sid = os.getenv("TWILIO_ACCOUNT_SID") 
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


parameters={
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_key,
    "exclude": "daily,current,minutely"
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
sliced_data = weather_data["hourly"][:13]

will_rain = False
for hour_data in sliced_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella :)",
        from_= "+18788880816",
        to="+447742200038"
    )

    print(message.status)

