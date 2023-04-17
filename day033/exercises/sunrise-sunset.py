import datetime
import pytz
import requests as requests

from lxml import html


def get_location():
    external_ip_response = requests.get('https://ident.me')
    external_ip_response.raise_for_status()
    external_ip = external_ip_response.content.decode("utf8")

    location_response = requests.get(f"https://ipgeolocation.io/ip-location/{external_ip}")
    location_response.raise_for_status()
    location_response_html = html.fromstring(location_response.content)
    city = location_response_html.xpath("string(//*[@id='ipInfoTable']/tbody/tr[12]/td[2])")
    country = location_response_html.xpath("string(//*[@id='ipInfoTable']/tbody/tr[7]/td[2])")
    latitude, longitude = location_response_html.xpath("string(//*[@id='ipInfoTable']/tbody/tr[14]/td[2])").split(",")

    return {
        "country": country,
        "city": city,
        "latitude": latitude,
        "longitude": longitude
    }


def main():
    # location = get_location()
    # print(f"It looks like you're in the city of {city}, {country} ({latitude} {longitude})")

    latitude = -18.91907
    longitude = -48.27833

    sunrise_sunset_request_parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0
    }
    sunrise_sunset_response = requests.get("https://api.sunrise-sunset.org/json",
                                           params=sunrise_sunset_request_parameters)
    sunrise_sunset_response.raise_for_status()
    sunrise_sunset_response = sunrise_sunset_response.json()

    sunrise_time = datetime.datetime.fromisoformat(sunrise_sunset_response["results"]["sunrise"])
    sunset_time = datetime.datetime.fromisoformat(sunrise_sunset_response["results"]["sunset"])
    now_time = datetime.datetime.now(pytz.utc)

    if sunrise_time.hour < now_time.hour < sunset_time.hour:
        print("It's currently day there ☀️")
    else:
        print("It's currently night there 🌙")


if __name__ == "__main__":
    main()
