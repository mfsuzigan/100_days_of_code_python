import re

import requests
from bs4 import BeautifulSoup

billboard_hot_100_URL = "https://www.billboard.com/charts/hot-100"


def main():
    destination_year = ""
    while not re.compile(r"\d{4}-\d{2}-\d{2}").match(destination_year):
        destination_year = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

    hot_100_request = requests.get(f"{billboard_hot_100_URL}/{destination_year}")
    hot_100_request.raise_for_status()

    soup = BeautifulSoup(hot_100_request.content, "html.parser")
    elements = soup.findAll(class_=re.compile("lrv-u-padding-l-1@mobile-max"))

    hot_100_list = [(normalize(element.find("span")), normalize(element.find("h3"))) for element in elements]
    print(hot_100_list)


def normalize(song_element):
    return song_element.text.replace("\n", "").replace("\t", "")


if __name__ == "__main__":
    main()
