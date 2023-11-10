import datetime
import logging
import os
import smtplib

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

    logging.info("Retrieving customers")
    customers = get_customers_data()

    notify(customers, date_from, date_to, affordable_flight_deals_by_city)

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


def notify(customers, date_from, date_to, affordable_deals_by_city):
    message = "Subject:Flight deals price alert\n"
    message += f"FULL_NAME,\nYou have a low price alert for flight deals from {date_from} to {date_to}!\n"

    for (destination, flights) in affordable_deals_by_city.items():
        logging.info(f"Found {len(flights)} affordable flights for destination {destination}")
        message += build_notification_message_for_destination(sorted(flights, key=lambda k: k["price"]))

    message += "\nEnjoy!"

    for customer in customers["users"]:
        send_email(message.replace("FULL_NAME", f"{customer['firstName']} {customer['lastName']}"),
                   customer["email"])


def build_notification_message_for_destination(affordable_deals_sorted_by_price):
    max_notifications_per_destination = int(os.environ["PROFILE_MAX_NOTIFICATIONS_PER_DESTINATION"])
    message = ""

    for notification_count, flight in enumerate(affordable_deals_sorted_by_price, start=1):

        if notification_count <= max_notifications_per_destination:
            message += (f"\n- Only {os.environ['PROFILE_CURRENCY']} ${flight['price']} "
                        f"to fly from {flight['cityFrom']}-{flight['cityCodeFrom']} "
                        f"to {flight['cityTo']}-{flight['cityCodeTo']}. ")

            stopover_info = f"Flight has 1 stopover via {flight['route'][0]['cityTo']}-{flight['route'][0]['flyTo']}" \
                if len(flight['route']) > 1 else ""

            message += stopover_info

        else:
            break

    return message


def send_email(message, to_address):
    with smtplib.SMTP(os.environ['SMTP_HOST'], int(os.environ['SMTP_PORT'])) as smtp_connection:
        smtp_connection.starttls()
        smtp_connection.login(user=os.environ['SMTP_USER'], password=os.environ['SMTP_PASSWORD'])
        smtp_connection.sendmail(from_addr=os.environ['SMTP_FROM_ADDRESS'], to_addrs=to_address,
                                 msg=message.encode(encoding="utf8"))

    logging.info(f"E-mail sent to user {to_address}")


def get_customers_data():
    response = requests.get(f"{os.environ['SHEETY_SHEET_ENDPOINT']}/users", headers=sheety_api_headers)
    response.raise_for_status()
    return response.json()


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
    response = requests.put(f"{os.environ['SHEETY_SHEET_ENDPOINT']}/prices/{city_current_data['id']}", json=body,
                            headers=sheety_api_headers)
    response.raise_for_status()
    return response.json()


def get_flight_sheet_data():
    response = requests.get(f"{os.environ['SHEETY_SHEET_ENDPOINT']}/prices", headers=sheety_api_headers)
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
