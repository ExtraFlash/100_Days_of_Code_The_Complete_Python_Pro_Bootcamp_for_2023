# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
import requests
from pprint import pprint
import datetime

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

notification_manager = NotificationManager()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# fill iata codes
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    # pprint(sheet_data)

    data_manager.update_local_destination_data(sheet_data=sheet_data)
    data_manager.update_destination_codes()

# search for flights from London to other destinations in Google Sheet
# pprint(data_manager.destination_data)
origin_airport = "LON"
out_date = datetime.datetime.today()
return_date = out_date + datetime.timedelta(days=180)

flight_search = FlightSearch()

for city in data_manager.destination_data:
    data = flight_search.check_flights(origin_city_code=origin_airport,
                                       destination_city_code=city['iataCode'],
                                       from_time=out_date,
                                       to_time=return_date)
    # pprint(data)
    flight_data = FlightData.find_cheapest_flight(data)
    if flight_data.price == "N/A":
        print(f'Not found a flight to {city["city"]}')
        continue
    print(f'Found a flight to {city["city"]} with a price of {flight_data.price}!')
    lowestPrice = float(city['lowestPrice'])
    price = float(flight_data.price)

    if price < lowestPrice:
        print(f"Price is lower than lowest price, sending an SMS message!")
        notification_manager.send_message(price=price,
                                          origin_airport=flight_data.origin_airport,
                                          destination_airport=flight_data.destination_airport,
                                          out_date=flight_data.out_date,
                                          return_date=flight_data.return_date)
