import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load env variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


class DataManager:

    def __init__(self):
        # self._user = os.getenv("SHEETY_USERNAME")
        # self._password = os.getenv("SHEETY_PASSWORD")
        # self._authorization_headers = os.getenv("SHEETY_AUTHORIZATION_HEADERS")
        # self._authorization = HTTPBasicAuth(self._user, self._password)
        self._token = os.getenv("SHEETY_TOKEN")
        self._prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
        self._users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self._prices_endpoint)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self._prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self._users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

