import os
import sys

import requests

sys.path.append(f"{os.path.dirname(__file__)}/..")
from pyutils.pyutils import get_configs

configs = {}


def main():
    global configs
    configs = get_configs(
        required_configs_set={"SHEETY_SHEET_ENDPOINT", "SHEETY_API_AUTH_TOKEN", "TEQUILA_API_ENDPOINT",
                              "TEQUILA_API_KEY"},
        path=f"{os.path.dirname(__file__)}")

    print(get_iata_code("Uberlandia"))


def get_iata_code(city_name):
    parameters = {
        "term": f"{city_name}",
        "location_types": "airport",
        "active_only": True
    }

    headers = {
        "accept": "application/json",
        "apikey": f"{configs['TEQUILA_API_KEY']}"
    }

    response = requests.get(f"{configs['TEQUILA_API_ENDPOINT']}/locations/query", params=parameters, headers=headers)
    response.raise_for_status()
    response = response.json()

    if len(response["locations"]) > 0:
        return response["locations"][0]["city"]["code"]

    else:
        return None


if __name__ == "__main__":
    main()
