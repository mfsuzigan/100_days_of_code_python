import datetime
import logging
import os

import requests
from dateutil.relativedelta import relativedelta

sheety_api_headers = {}
tequila_api_headers = {}


def main():
    setup()

    now = datetime.datetime.now()
    date_from = (now + datetime.timedelta(days=1)).strftime("%d/%m/%Y")

    flight_search_period_months = int(os.environ["PROFILE_FLIGHT_DEALS_SEARCH_PERIOD_MONTHS"])
    date_to = (now + relativedelta(months=flight_search_period_months)).strftime("%d/%m/%Y")

    logging.info("Checking for affordable flight deals")
    affordable_flight_deals_by_city = get_affordable_flight_deals(date_from, date_to)

    for (destination, flights) in affordable_flight_deals_by_city.items():
        logging.info(f"Found {len(flights)} affordable flights for destination {destination}")
        notify(date_from, date_to, flights)

    logging.info("Done!")


def setup():
    logging.basicConfig(level=logging.INFO)

    global sheety_api_headers
    sheety_api_headers = {"Authorization": f"Bearer {os.environ['SHEETY_API_AUTH_TOKEN']}"}

    global tequila_api_headers
    tequila_api_headers = {
        "accept": "application/json",
        "apikey": f"{os.environ['TEQUILA_API_KEY']}"
    }

    set_departure_city_iata_code()


def set_departure_city_iata_code():
    os.environ['PROFILE_DEPARTURE_CITY_IATA_CODE'] = get_iata_code(os.environ['PROFILE_DEPARTURE_CITY'])

    if not os.environ['PROFILE_DEPARTURE_CITY_IATA_CODE']:
        raise Exception(f"IATA code not found for departure city {os.environ['PROFILE_DEPARTURE_CITY']}")

    else:
        logging.info(
            f"IATA code {os.environ['PROFILE_DEPARTURE_CITY_IATA_CODE']} set for departure city "
            f"{os.environ['PROFILE_DEPARTURE_CITY']}")


def notify(date_from, date_to, affordable_deals):
    max_notifications = int(os.environ["PROFILE_MAX_NOTIFICATIONS_PER_DESTINATION"])
    affordable_deals_sorted_by_price = sorted(affordable_deals, key=lambda k: k["price"])

    for notification_count, flight in enumerate(affordable_deals_sorted_by_price, start=1):

        if notification_count <= max_notifications:
            message = (
                f"Low price alert! Only {os.environ['PROFILE_CURRENCY']} ${flight['price']} "
                f"to fly from {flight['cityFrom']}-{flight['cityCodeFrom']} "
                f"to {flight['cityTo']}-{flight['cityCodeTo']}, "
                f"from {date_from} to {date_to}. ")

            stopover_info = f"Flight has 1 stopover via {flight['route'][0]['cityTo']}-{flight['route'][0]['flyTo']}" \
                if len(flight['route']) > 1 else ""

            logging.info(message + stopover_info)

            # TODO: send email

        else:
            break


def get_affordable_flight_deals(date_from, date_to):
    flight_sheet_data = get_flight_sheet_data()

    affordable_flight_deals_by_city = {}

    for flight_price in flight_sheet_data["prices"]:

        if "lowestPrice" not in flight_price or flight_price['lowestPrice'] == '':
            logging.warning(f"Target price for destination {flight_price['city']} not set, skipping")
            continue

        if "iataCode" not in flight_price or flight_price['iataCode'] == '':
            iata_code = get_iata_code(flight_price["city"])
            logging.info(f"Setting IATA code {iata_code} for destination {flight_price['city']}")
            put_flight_city_iata_code(iata_code, flight_price)

        affordable_flight_deals_by_city[flight_price["city"]] = get_flight_deals(
            flight_price["iataCode"], date_from, date_to,
            flight_price["lowestPrice"])["data"]

    return affordable_flight_deals_by_city


def get_flight_deals(fly_to, date_from, date_to, lowest_price):
    parameters = {
        "fly_from": os.environ['PROFILE_DEPARTURE_CITY_IATA_CODE'],
        "fly_to": fly_to,
        "date_from": date_from,
        "date_to": date_to,
        "curr": os.environ["PROFILE_CURRENCY"],
        "price_to": lowest_price,
        "max_stopovers": 1
    }

    response = requests.get(f"{os.environ['TEQUILA_API_ENDPOINT']}/v2/search", params=parameters,
                            headers=tequila_api_headers)
    response.raise_for_status()
    return response.json()


def put_flight_city_iata_code(city_iata_code, city_current_data):
    city_current_data["iataCode"] = city_iata_code
    body = {"price": city_current_data}
    response = requests.put(f"{os.environ['SHEETY_SHEET_ENDPOINT']}/{city_current_data['id']}", json=body,
                            headers=sheety_api_headers)
    response.raise_for_status()
    return response.json()


def get_flight_sheet_data():
    response = requests.get(os.environ["SHEETY_SHEET_ENDPOINT"], headers=sheety_api_headers)
    response.raise_for_status()
    return response.json()


def get_iata_code(city_name):
    parameters = {
        "term": f"{city_name}",
        "location_types": "airport",
        "active_only": True
    }

    response = requests.get(
        f"{os.environ['TEQUILA_API_ENDPOINT']}/locations/query",
        params=parameters,
        headers=tequila_api_headers)
    response.raise_for_status()
    response = response.json()

    if len(response["locations"]) > 0:
        return response["locations"][0]["city"]["code"]

    else:
        return None


if __name__ == "__main__":
    main()
