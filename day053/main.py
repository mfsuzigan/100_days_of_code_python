# Google form link: https://docs.google.com/forms/d/e/1FAIpQLSecQASe_yUqFMglETPq_HzRXTOaB8h6BoyCC1h2bgoWzyZ93Q/viewform?usp=sf_link
import re

import requests
from bs4 import BeautifulSoup
from models.rental_listing import RentalListing

RENTING_WEBSITE_LOCATION = "https://appbrewery.github.io/Zillow-Clone/"


def main():
    for listing in get_renting_website_data():
        anchor_element = listing.findNext(name="a")
        address = anchor_element.text.strip()
        link = anchor_element.attrs["href"]
        price = re.search(r"^\$\d*,*\d*", listing.findNext(name="span").text).group()
        write_to_spreadsheet(RentalListing(price=price, address=address, link=link))


def write_to_spreadsheet(rental_listing):
    pass


def get_renting_website_data():
    soup = BeautifulSoup(requests.get(RENTING_WEBSITE_LOCATION).content, "html.parser")
    return soup.find_all(class_=re.compile("ListItem"))


if __name__ == "__main__":
    main()
