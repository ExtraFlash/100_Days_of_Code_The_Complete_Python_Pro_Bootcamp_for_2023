import requests
from datetime import datetime

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

pixela_endpoint = os.getenv("PIXELA_ENDPOINT")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

now = datetime.now()
date_formatted = now.strftime("%Y%m%d")

pixel_data = {
    "date": date_formatted,
    "quantity": "5"
}

# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date_formatted}"

pixel_update_data = {
    "quantity": "10.8",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = pixel_update_endpoint

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
