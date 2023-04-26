import argparse
import datetime
import smtplib
import pytz
import requests as requests
import time

from lxml import html

SLEEP_TIME_SECONDS = 60 * 2


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
        "latitude": float(latitude),
        "longitude": float(longitude)
    }


def check_daytime(latitude, longitude):
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
    return sunrise_time < now_time < sunset_time


def check_iss_near(latitude, longitude):
    iss_now_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_now_response.raise_for_status()
    iss_now_response = iss_now_response.json()

    iss_longitude = float(iss_now_response["iss_position"]["longitude"])
    iss_latitude = float(iss_now_response["iss_position"]["latitude"])

    within_longitude = -5 < iss_longitude - longitude < 5
    within_latitude = -5 < iss_latitude - latitude < 5

    return within_longitude and within_latitude


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--from-email", "-f", required=True, help="Sender's email")
    arg_parser.add_argument("--password", "-p", required=True, help="Password for sender's email")
    arg_parser.add_argument("--smtp", "-s", required=True, help="Sender's SMTP server")
    arg_parser.add_argument("--to-email", "-t", required=True, help="Recipient's email")

    return arg_parser.parse_args()


def send_email(args):
    message = "Subject:Look up for the ISS!!\n"
    message += "Greetings," \
               "\nWe have determined that you should be able to see the Internation Space Station this night!" \
               "\n" \
               "\nGood luck," \
               "\nPythonist"

    with smtplib.SMTP(args.smtp, 587) as smtp_connection:
        smtp_connection.starttls()
        smtp_connection.login(user=args.from_email, password=args.password)
        smtp_connection.sendmail(from_addr=args.from_email, to_addrs=args.to_email, msg=message)


def main():
    args = get_args()
    location = get_location()

    print(
        f"\nIt looks like you're in the city of {location['city']}, {location['country']} "
        f"({location['latitude']} {location['longitude']}) 🌎")

    while True:
        is_daytime = check_daytime(location['latitude'], location['longitude'])
        iss_sight_successful = False

        if is_daytime:
            print("It's currently daytime there ☀️")

        else:
            print("It's currently nighttime there 🌙")
            is_iss_near = check_iss_near(location["latitude"], location["longitude"])

            if is_iss_near:
                print("The International Space Station is near! 🛰")
                print("\nSending heads-up e-mail...\n")

                send_email(args)

                print("Done")
                iss_sight_successful = True

            else:
                print("Unfortunately, the International Space Station is not near ❌")

        if not iss_sight_successful:
            print("\nIt's not possible to see the ISS at the time.\n")

        print("Sleeping now...\n")
        time.sleep(SLEEP_TIME_SECONDS)


if __name__ == "__main__":
    main()
