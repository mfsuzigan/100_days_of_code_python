import datetime
import os
import sys
import pytz
import requests

sys.path.append(f"{os.path.dirname(__file__)}/..")
from pyutils.pyutils import get_configs
from pyutils.pyutils import send_twilio_sms

THREE_HOURS_PERIODS_TO_EXAMINE = 3
OPENWEATHER_FORECAST_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
REQUIRED_CONFIGURATION_KEYS = {"WEATHER_API_KEY", "TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "SENDER_PHONE",
                               "RECIPIENT_PHONE",
                               "LOCATION_LATITUDE", "LOCATION_LONGITUDE"}


def main():
    configs = get_configs(REQUIRED_CONFIGURATION_KEYS)

    forecast = get_forecast(configs)
    rain_is_expected = {forecast['rain_is_expected']}
    details = str.join("\n", [d for d in forecast['results']])

    print(f"** Forecast results **\n"
          f"Rain expected: {rain_is_expected}\n"
          f"Details:\n{details}")

    if rain_is_expected:
        print("Sending SMS...")
        forecast_details = str.join('\n ', forecast['results'])
        send_twilio_sms(f"Rain PyAlert\n{forecast_details}", configs)
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
