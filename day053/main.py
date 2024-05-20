import re

import requests
from bs4 import BeautifulSoup
from models.rental_listing import RentalListing

from selenium.webdriver.common.by import By
from selenium import webdriver

RENTING_WEBSITE_LOCATION = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LOCATION = ("https://docs.google.com/forms/d/e/"
                 "1FAIpQLSecQASe_yUqFMglETPq_HzRXTOaB8h6BoyCC1h2bgoWzyZ93Q/viewform?usp=sf_link")


def main():
    write_to_spreadsheet(
        [to_rental_listing_model(d) for d in get_renting_website_data()])


def to_rental_listing_model(listing):
    anchor_element = listing.findNext(name="a")
    address = anchor_element.text.strip()
    link = anchor_element.attrs["href"]
    price = float(re.search(r"^\$\d*,*\d*", listing.findNext(name="span").text)
                  .group()
                  .replace("$", "")
                  .replace(",", ""))
    return RentalListing(price=price, address=address, link=link)


def write_to_spreadsheet(rental_listings: RentalListing):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(FORM_LOCATION)

    for rental_listing in rental_listings:
        text_inputs = driver.find_elements(By.XPATH,
                                           "//div[text()='Sua resposta']/ancestor::div/input[@type='text']")

        [text_input.send_keys(text) for text_input, text in
         zip(text_inputs, [rental_listing.address, rental_listing.price, rental_listing.link])]

        driver.find_element(By.XPATH, "//span[text()='Enviar']").click()
        driver.find_element(By.XPATH, "//a[text()='Enviar outra resposta']").click()


def get_renting_website_data():
    soup = BeautifulSoup(requests.get(RENTING_WEBSITE_LOCATION).content, "html.parser")
    return soup.find_all(class_=re.compile("ListItem"))


def get_webdriver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")

    return webdriver.Chrome(options=options)


if __name__ == "__main__":
    main()
