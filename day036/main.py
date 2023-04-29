import argparse
import logging
import requests
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

ALPHA_ADVANTAGE_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
FMP_API_ENDPOINT = "https://financialmodelingprep.com/api/v3/search"
PRICE_PERCENT_VARIATION_TRIGGER_THRESHOLD = 0


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_price_variation(stock_ticker, stock_prices_api):
    request_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK_TICKER,
        "apikey": STOCK_PRICES_API_KEY,
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
        logging.exception(f"There was a problem calculating price variation for stock {STOCK_TICKER}")


def main():
    configurations = get_configs()
    stock_ticker = get_args().stock_ticker

    price_variation = get_stock_price_variation()
    alert_message = None

    if price_variation >= PRICE_PERCENT_VARIATION_TRIGGER_THRESHOLD:
        stock_name = get_stock_name(stock_ticker=stock_ticker)
        news_list = get_stock_news(stock_name)[:3]
        alert_message = f"{stock_ticker}: {'🔺' if price_variation > 0 else '🔻'}{price_variation :.2f}%\n"

        for news in news_list:
            alert_message += f"Headline: {news['title']}\nBrief: {news['description']}\n"

    if alert_message:
        pass


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_stock_news_api_parameters(stock_name):
    return {
        "apiKey": NEWS_API_KEY,
        "q": stock_name,
        "country": "us"
    }


def get_stock_news(stock_name):
    news_list = request_stock_news_api(stock_name)

    if len(news_list) == 0:
        stock_name = str.join(" ", stock_name.lower().replace("inc", "").replace("the", "").split(" ")[:2])
        news_list = request_stock_news_api(stock_name)

    if len(news_list) == 0 and len(stock_name.split(" ")) > 1:
        stock_name = stock_name.split(" ")[0]
        news_list = request_stock_news_api(stock_name)

    return news_list


def request_stock_news_api(stock_name):
    response = requests.get(NEWS_API_ENDPOINT, get_stock_news_api_parameters(stock_name))
    response.raise_for_status()
    news_list = response.json()["articles"][:3]
    return news_list


def get_stock_name(stock_ticker):
    parameters = {
        "query": stock_ticker,
        "limit": 1,
        "exchange": "NYSE",
        "apikey": "8367e695e5ecb9a7deecb72526b6ef1e"
    }

    response = requests.get(FMP_API_ENDPOINT, params=parameters)
    response.raise_for_status()
    response = response.json()

    stock_name = None

    if len(response) > 0:
        stock_name = response[0]["name"]

    return stock_name


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_sms(configs, message):
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
