import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self._account_sid = os.getenv("TWILIO_account_sid")
        self._auth_token = os.getenv("TWILIO_auth_token")
        self._sender_phone_number = os.getenv("SENDER_PHONE_NUMBER")
        self._receiver_phone_number = os.getenv("RECEIVER_PHONE_NUMBER")
        self._client = Client(self._account_sid, self._auth_token)

    def send_message(self, price, origin_airport, destination_airport, out_date, return_date):

        message = self._client.messages.create(
            body=f"Low price alert! Only {price} to fly"
                 f"from {origin_airport} to {destination_airport}, on "
                 f"{out_date} until {return_date}.",
            from_=self._sender_phone_number,
            to=self._receiver_phone_number
        )
