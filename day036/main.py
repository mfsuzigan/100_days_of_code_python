import argparse
import logging
import requests
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

ALPHA_ADVANTAGE_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
FMP_API_ENDPOINT = "https://financialmodelingprep.com/api/v3/search"
PRICE_PERCENTUAL_VARIATION_THRESHOLD = 5


def get_stock_price_variation(stock_ticker, stock_prices_api_key):
    request_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock_ticker,
        "apikey": stock_prices_api_key,
    }

    response = requests.get(ALPHA_ADVANTAGE_API_ENDPOINT, request_parameters)
    response.raise_for_status()
    response = response.json()

    stock_price_series = list(response["Time Series (Daily)"])
    stock_price_series.sort(reverse=True)

    stock_price_series = stock_price_series[:2]

    try:
        price_base = float(response["Time Series (Daily)"][stock_price_series[1]]["4. close"])
        price_final = float(response["Time Series (Daily)"][stock_price_series[0]]["4. close"])
        return 100 * (price_final / price_base - 1)

    except (KeyError, ValueError):
        logging.exception(f"There was a problem calculating price variation for stock {stock_ticker}")


def main():
    configurations = get_configs()
    stock_ticker = get_args().stock_ticker

    price_variation = get_stock_price_variation(stock_ticker=stock_ticker,
                                                stock_prices_api_key=configurations["ALPHA_ADVANTAGE_API_KEY"])

    normalized_price_variation = price_variation if price_variation >= 0 else -1 * price_variation

    print(
        f"Variation detected for stock {stock_ticker}: {price_variation :.2f}% "
        f"(threshold is +/-{PRICE_PERCENTUAL_VARIATION_THRESHOLD}%)")

    alert_message = None

    if normalized_price_variation >= PRICE_PERCENTUAL_VARIATION_THRESHOLD:
        stock_name = get_stock_name(stock_ticker=stock_ticker, stock_name_api_key=configurations["FMP_API_KEY"])
        news_list = get_stock_news(stock_name, news_api_key=configurations["NEWS_API_KEY"])[:3]
        alert_message = f"{stock_ticker}: {'🔺' if price_variation > 0 else '🔻'}{price_variation :.2f}%\n"

        print(f"Found {len(news_list)} news pieces for {stock_name}")

        for news in news_list:
            alert_message += f"Headline: {news['title']}\nBrief: {news['description']}\n"

    else:
        print("No action taken")

    if alert_message:
        print("Sending SMS...")
        send_sms(configurations, alert_message)

    print("Done")


def get_stock_news_api_parameters(stock_name, news_api_key):
    return {
        "apiKey": news_api_key,
        "q": stock_name,
        "country": "us"
    }


def normalize_stock_name(stock_name):
    normalized_name = stock_name.strip().lower()

    for term in ["inc", ",", ".", "the"]:
        normalized_name = normalized_name.replace(term, "")

    return normalized_name.strip()


def get_stock_news(stock_name, news_api_key):
    normalized_stock_name = normalize_stock_name(stock_name)
    news_list = request_stock_news_api(normalized_stock_name, news_api_key)

    if len(news_list) == 0:
        # zero news, fallback by taking first two words of name
        normalized_stock_name = str.join("", normalized_stock_name.split(" ")[:2])
        news_list = request_stock_news_api(normalized_stock_name, news_api_key)

    if len(news_list) == 0 and len(normalized_stock_name.split(" ")) > 1:
        # still zero news, fallback by taking first word of name
        normalized_stock_name = stock_name.split(" ")[0]
        news_list = request_stock_news_api(normalized_stock_name, news_api_key)

    return news_list


def request_stock_news_api(stock_name, news_api_key):
    response = requests.get(NEWS_API_ENDPOINT, get_stock_news_api_parameters(stock_name, news_api_key))
    response.raise_for_status()
    news_list = response.json()["articles"][:3]
    return news_list


def get_stock_name(stock_ticker, stock_name_api_key):
    parameters = {
        "query": stock_ticker,
        "limit": 1,
        "apikey": stock_name_api_key
    }

    stock_name = None

    for exchange in ["NYSE", "NASDAQ"]:
        parameters["exchange"] = exchange
        response = request_stock_name_api(parameters)

        if len(response) > 0:
            stock_name = response[0]["name"]
            break

    return stock_name


def request_stock_name_api(parameters):
    response = requests.get(FMP_API_ENDPOINT, params=parameters)
    response.raise_for_status()
    response = response.json()
    return response


def send_sms(configs, text):
    client = Client(configs["TWILIO_ACCOUNT_SID"], configs["TWILIO_AUTH_TOKEN"])

    try:
        message = client.messages.create(
            body=f"{text}",
            from_=configs["SENDER_PHONE"],
            to=configs["RECIPIENT_PHONE"]
        )
        print(f"SMS sent, ID {message.sid}")

    except TwilioRestException:
        logging.exception("Error sending stock alert SMS")


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--stock-ticker", "-s", required=True, help="Ticker of the stock to be examined")

    return arg_parser.parse_args()


def get_configs():
    required_configs = ["TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN",
                        "SENDER_PHONE", "RECIPIENT_PHONE", "ALPHA_ADVANTAGE_API_KEY",
                        "NEWS_API_KEY", "FMP_API_KEY"]

    try:
        with open("configurations.ini") as configurations_file:
            configs = {key: value for (key, value) in
                       [line.strip().split("=") for line in configurations_file.readlines()]}

    except FileNotFoundError:
        logging.exception("Error reading configuration files")

    if not set(required_configs).issubset(configs):
        raise Exception(f"One or more configurations not found in configurations.ini: {required_configs}")

    return configs


if __name__ == "__main__":
    main()
