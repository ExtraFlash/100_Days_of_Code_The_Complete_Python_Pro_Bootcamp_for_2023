import os
import requests
from dotenv import load_dotenv

from pprint import pprint

# Load env variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/6bc3c104079e0d72c3eae6ad72f60ca5/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # get all data from sheet
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        data = response.json()

        self.destination_data = data['prices']

        return self.destination_data

    def update_local_destination_data(self, sheet_data):
        self.destination_data = sheet_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }

            response = requests.put(
                url=f'{SHEETY_PRICES_ENDPOINT}/{city["id"]}',
                json=new_data
            )

            response.raise_for_status()
