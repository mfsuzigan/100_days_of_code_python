import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF/ref=sr_1_1?crid=1URLG662SWBRT&keywords=system+design+interview&qid=1700788315&sprefix=system+design+interview%2Caps%2C354&sr=8-1"


def main():
    request_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.7"
    }
    product_page = requests.get(PRODUCT_URL, headers=request_headers).content
    soup = BeautifulSoup(product_page, "html.parser")
    print(soup)


if __name__ == '__main__':
    main()
