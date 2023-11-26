import logging
import os
import smtplib
import sys
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ITEM_URL = "https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF/ref=sr_1_1"


def main():
    logging.basicConfig(level=logging.INFO)
    verify_required_env()

    logging.info("Searching for item on Amazon...")
    soup = get_amazon_item_soup(ITEM_URL)
    item_prices = soup.findAll(name="span", class_="a-price")

    if len(item_prices) > 0:
        price = extract_item_price(item_prices[0])

        if price <= float(os.environ.get("ITEM_TARGET_PRICE")):
            logging.info("Item price within threshold, sending e-mail")
            item_name = soup.find(id="title").text.replace("\n", "")
            send_email(build_notification_message(item_name, price, ITEM_URL))

        else:
            logging.info("Item price not within threshold")

    else:
        logging.info("Item not found")

    logging.info("Done")


def build_notification_message(item_name, price, item_url):
    message = "Subject:Price alert\n"
    message += (f"Hi, \n"
                f"Item \"{item_name}\" is now {price}. \n"
                "Link: \n"
                f"{item_url}")

    return message


def extract_item_price(target_price):
    return int(target_price.find(class_="a-price-whole").next_element) + int(
        target_price.find(class_="a-price-fraction").text) / 100


def get_amazon_item_soup(item_url):
    request_headers = {
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    ua = UserAgent(browsers=['edge', 'chrome'])
    user_agent = ua.random

    while True:
        request_headers["User-Agent"] = user_agent
        product_page = requests.get(item_url, headers=request_headers).text

        if "api-services-support@amazon.com" in product_page:
            user_agent = ua.random

        else:
            return BeautifulSoup(product_page, "html.parser")


def verify_required_env():
    required_env_vars = ["ITEM_TARGET_PRICE", "RECEIVER_EMAIL", "SMTP_HOST", "SMTP_PORT", "SMTP_USER", "SMTP_PASSWORD",
                         "SMTP_FROM_ADDRESS"]
    not_set_env_vars = [v for v in required_env_vars if not os.getenv(v)]

    if len(not_set_env_vars) > 0:
        logging.error(f"Fatal: required environment variables not set: {not_set_env_vars}")
        sys.exit(1)


def send_email(message):
    with smtplib.SMTP_SSL(os.environ['SMTP_HOST'], int(os.environ['SMTP_PORT'])) as smtp_connection:
        smtp_connection.login(user=os.environ['SMTP_USER'], password=os.environ['SMTP_PASSWORD'])
        smtp_connection.sendmail(from_addr=os.environ['SMTP_FROM_ADDRESS'], to_addrs=os.environ['RECEIVER_EMAIL'],
                                 msg=message.encode(encoding="utf8"))


if __name__ == '__main__':
    main()
