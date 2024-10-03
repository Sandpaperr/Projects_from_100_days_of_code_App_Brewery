from datetime import datetime

import requests
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = os.getenv("PIXELA_ENDPOINT")
token = os.getenv("PIXELA_TOKEN")
username = os.getenv("PIXELA_USERNAME")
graph_name = "graph1"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": graph_name,
    "name": "coding Graph",
    "unit": "days",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint,headers=headers, json=graph_config)
# print(response.text)

pixel_config = {
    "date": datetime.now().date().strftime("%Y%m%d"),
    "quantity": "1",
}

one_pixel_endpoint =f"{pixela_endpoint}/{username}/graphs/{graph_name}"

response = requests.post(url=one_pixel_endpoint, headers=headers, json=pixel_config)
print(response.text)
print(one_pixel_endpoint)