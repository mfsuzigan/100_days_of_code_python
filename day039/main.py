import datetime
import os
import sys
import logging
from dateutil.relativedelta import relativedelta

import requests

sys.path.append(f"{os.path.dirname(__file__)}/..")
from pyutils.pyutils import get_configs

configs = {}
sheety_api_headers = {}
tequila_api_headers = {}


def main():
    setup()
    affordable_flight_deals = check_affordable_flight_deals()

    for (destination, flights) in affordable_flight_deals.items():
        logging.info(f"Found {len(flights)} affordable flights for destination {destination}")


def setup():
    logging.basicConfig(level=logging.INFO)

    global configs
    configs = get_configs(
        required_configs_set={"SHEETY_SHEET_ENDPOINT", "SHEETY_API_AUTH_TOKEN", "TEQUILA_API_ENDPOINT",
                              "TEQUILA_API_KEY", "PROFILE_DEPARTURE_CITY"},
        path=f"{os.path.dirname(__file__)}")

    global sheety_api_headers
    sheety_api_headers = {"Authorization": f"Bearer {configs['SHEETY_API_AUTH_TOKEN']}"}

    global tequila_api_headers
    tequila_api_headers = {"accept": "application/json", "apikey": f"{configs['TEQUILA_API_KEY']}"}

    set_departure_city_iata_code()


def set_departure_city_iata_code():
    configs['PROFILE_DEPARTURE_CITY_IATA_CODE'] = get_iata_code(configs['PROFILE_DEPARTURE_CITY'])

    if not configs['PROFILE_DEPARTURE_CITY_IATA_CODE']:
        raise Exception(f"IATA code not found for departure city {configs['PROFILE_DEPARTURE_CITY']}")

    else:
        logging.info(
            f"IATA code {configs['PROFILE_DEPARTURE_CITY_IATA_CODE']} set for departure city "
            f"{configs['PROFILE_DEPARTURE_CITY']}")


def check_affordable_flight_deals():
    flight_sheet_data = get_flight_sheet_data()
    affordable_flight_deals = {}

    now = datetime.datetime.now()
    date_from = (now + datetime.timedelta(days=1)).strftime("%d/%m/%Y")

    flight_search_period_months = int(configs["PROFILE_FLIGHT_DEALS_SEARCH_PERIOD_MONTHS"])
    date_to = (now + relativedelta(months=flight_search_period_months)).strftime("%d/%m/%Y")

    for flight_price in flight_sheet_data["prices"]:

        if not flight_price["lowestPrice"]:
            logging.warning(f"Target price for destination city {flight_price['city']} not set, skipping")
            continue

        if not flight_price["iataCode"]:
            iata_code = get_iata_code(flight_price["city"])
            logging.info(f"Setting IATA code {iata_code} for destination city {flight_price['city']}")
            put_flight_city_iata_code(iata_code, flight_price)

        affordable_flight_deals[flight_price["city"]] = get_flight_deals(flight_price["iataCode"], date_from, date_to,
                                                                         flight_price["lowestPrice"])["data"]

    return affordable_flight_deals


def get_flight_deals(fly_to, date_from, date_to, lowest_price):
    parameters = {
        "fly_from": f"{configs['PROFILE_DEPARTURE_CITY_IATA_CODE']}",
        "fly_to": fly_to,
        "date_from": date_from,
        "date_to": date_to,
        "curr": configs.get("PROFILE_CURRENCY"),
        "price_to": lowest_price
    }

    response = requests.get(f"{configs['TEQUILA_API_ENDPOINT']}/v2/search", params=parameters,
                            headers=tequila_api_headers)
    response.raise_for_status()
    return response.json()


def put_flight_city_iata_code(city_iata_code, city_current_data):
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
