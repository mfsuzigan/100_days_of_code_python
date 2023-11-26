import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

PRODUCT_URL = "https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF/ref=sr_1_1"


def main():
    request_headers = {
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    ua = UserAgent(browsers=['edge', 'chrome'])
    user_agent = ua.random

    while True:
        request_headers["User-Agent"] = user_agent
        product_page = requests.get(PRODUCT_URL, headers=request_headers).text

        if "api-services-support@amazon.com" in product_page:
            user_agent = ua.random

        else:
            soup = BeautifulSoup(product_page, "html.parser")
            print(soup)
            break


if __name__ == '__main__':
    main()
