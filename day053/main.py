# Google form link: https://docs.google.com/forms/d/e/1FAIpQLSecQASe_yUqFMglETPq_HzRXTOaB8h6BoyCC1h2bgoWzyZ93Q/viewform?usp=sf_link
import requests
from bs4 import BeautifulSoup
from models.rental_listing import RentalListing


def main():
    # scrape site
    # process data
    # send data to form
    pass


def to_rental_listings(raw_data):
    for listing in raw_data:
        price = 0
        address = ""
        link = ""
        RentalListing(price, address, link)


def get_rental_listings_data():
    soup = BeautifulSoup(requests.get(""), "html.parser")
    raw_data = soup.find_all(name="li")
    rental_listings = to_rental_listings(raw_data)
    return rental_listings
