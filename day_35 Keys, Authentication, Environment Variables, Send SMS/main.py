import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# twilio
account_sid = os.getenv("TWILIO_account_sid")
auth_token = os.getenv("TWILIO_auth_token")

# weather
OWM_Endpoint = os.getenv("OPENWEATHER_Endpoint")
api_key = os.getenv("OPENWEATHER_api_key")

params = {
    'lat': -51.7,
    'lon': 1.27,
    'cnt': 4,
    'appid': api_key
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
weather_data_list = response.json()['list']

will_rain = False
for hour_data in weather_data_list:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+12564459255',
        to='+972552212114'
    )

    print(message.sid)
