import os
import sys
import logging

import requests

sys.path.append(f"{os.path.dirname(__file__)}/..")
from pyutils.pyutils import get_configs

configs = {}
sheety_api_headers = {}
tequila_api_headers = {}


def main():
    setup()
    check_affordable_flight_deals()


def setup():
    logging.basicConfig(level=logging.INFO)

    global configs
    configs = get_configs(
        required_configs_set={"SHEETY_SHEET_ENDPOINT", "SHEETY_API_AUTH_TOKEN", "TEQUILA_API_ENDPOINT",
                              "TEQUILA_API_KEY"},
        path=f"{os.path.dirname(__file__)}")

    global sheety_api_headers
    sheety_api_headers = {
        "Authorization": f"Bearer {configs['SHEETY_API_AUTH_TOKEN']}"
    }

    global tequila_api_headers
    tequila_api_headers = {
        "accept": "application/json",
        "apikey": f"{configs['TEQUILA_API_KEY']}"
    }


def check_affordable_flight_deals():
    flight_sheet_data = get_flight_sheet_data()

    for flight_price in flight_sheet_data["prices"]:

        if not flight_price["lowestPrice"]:
            logging.warning(f"Target price for destionation city {flight_price['city']} not set, skipping")
            continue

        if not flight_price["iataCode"]:
            logging.info(f"Retrieving IATA code for destination city {flight_price['city']}")
            iata_code = get_iata_code(flight_price["city"])
            logging.info(f"Updating IATA code ({iata_code}) for destination city {flight_price['city']}")
            set_flight_city_iata_code(iata_code, flight_price)

    # check if iata code is present
    # if not, fill it

    # query for flight deals
    # if any exist, check prices below target and return them

    pass


def set_flight_city_iata_code(city_iata_code, city_current_data):
    city_current_data["iataCode"] = city_iata_code
    body = {
        "price": city_current_data
    }
    response = requests.put(f"{configs['SHEETY_SHEET_ENDPOINT']}/{city_current_data['id']}", json=body)
    response.raise_for_status()
    return response.json()


def get_flight_sheet_data():
    response = requests.get(configs["SHEETY_SHEET_ENDPOINT"], headers=sheety_api_headers)
    response.raise_for_status()
    return response.json()


def get_iata_code(city_name):
    parameters = {
        "term": f"{city_name}",
        "location_types": "airport",
        "active_only": True
    }

    response = requests.get(f"{configs['TEQUILA_API_ENDPOINT']}/locations/query", params=parameters,
                            headers=tequila_api_headers)
    response.raise_for_status()
    response = response.json()

    if len(response["locations"]) > 0:
        return response["locations"][0]["city"]["code"]

    else:
        return None


if __name__ == "__main__":
    main()
