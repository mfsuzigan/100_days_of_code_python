from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
import datetime
import logging

import pytz
import requests

THREE_HOURS_PERIODS_TO_EXAMINE = 3
OPENWEATHER_FORECAST_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"


def get_configs():
    required_configs = ["WEATHER_API_KEY", "TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "SENDER_PHONE", "RECIPIENT_PHONE",
                        "LOCATION_LATITUDE", "LOCATION_LONGITUDE"]

    try:
        with open("configurations.ini") as configurations_file:
            configs = {key: value for (key, value) in
                       [line.strip().split("=") for line in configurations_file.readlines()]}

    except FileNotFoundError:
        logging.exception("Error reading configuration files")

    if not set(required_configs).issubset(configs):
        raise Exception(f"One or more configurations not found in configurations.ini: {required_configs}")

    return configs


def send_sms(configs, forecast_details):
    client = Client(configs["TWILIO_ACCOUNT_SID"], configs["TWILIO_AUTH_TOKEN"])
    forecast_details = str.join("\n ", forecast_details)

    try:
        message = client.messages.create(
            body=f"Rain PyAlert\n{forecast_details}",
            from_=configs["SENDER_PHONE"],
            to=configs["RECIPIENT_PHONE"]
        )
        print(f"SMS sent, ID {message.sid}")

    except TwilioRestException:
        logging.exception("Error sending SMS Rain PyAlert")


def main():
    configs = get_configs()

    forecast = get_forecast(configs)
    rain_is_expected = {forecast['rain_is_expected']}
    details = str.join("\n", [d for d in forecast['results']])

    print(f"** Forecast results **\n"
          f"Rain expected: {rain_is_expected}\n"
          f"Details:\n{details}")

    if rain_is_expected:
        print("Sending SMS...")
        send_sms(configs, forecast['results'])
        print("Done")


def get_forecast(configs):
    parameters = {
        "lat": configs["LOCATION_LATITUDE"],
        "lon": configs["LOCATION_LONGITUDE"],
        "appid": configs["WEATHER_API_KEY"]
    }

    response = requests.get(OPENWEATHER_FORECAST_ENDPOINT, params=parameters)
    response.raise_for_status()
    response = response.json()

    forecast_items = response["list"]
    rain_expected = False
    forecast_results = []

    for forecast_item in forecast_items[:THREE_HOURS_PERIODS_TO_EXAMINE]:
        conditions = []

        for weather_item in forecast_item["weather"]:
            conditions.append(f"{weather_item['description']}")

            if not rain_expected and int(weather_item["id"]) < 700:
                rain_expected = True

        time = datetime.datetime.strptime(forecast_item['dt_txt'], "%Y-%m-%d %H:%M:%S")
        formatted_time = time.astimezone(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m %H:%M')
        forecast_results.append(
            f"{formatted_time} {str.join(', ', conditions)} 🌧️ {forecast_item['pop'] :.0%}")

    return {
        "rain_is_expected": rain_expected,
        "results": forecast_results
    }


if __name__ == "__main__":
    main()
