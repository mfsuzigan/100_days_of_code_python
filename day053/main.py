import re

import requests
import logging
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait

from models.rental_listing import RentalListing
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec

WEBDRIVER_RENDER_TIMEOUT_SECONDS = 5
RENTING_WEBSITE_LOCATION = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LOCATION = ("https://docs.google.com/forms/d/e/"
                 "1FAIpQLSecQASe_yUqFMglETPq_HzRXTOaB8h6BoyCC1h2bgoWzyZ93Q/viewform?usp=sf_link")


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting...")
    write_to_spreadsheet(
        [to_rental_listing_model(d) for d in get_renting_website_data()])
    logging.info("Finished!")


def to_rental_listing_model(listing):
    anchor_element = listing.findNext(name="a")
    address = anchor_element.text.strip()
    link = anchor_element.attrs["href"]
    price = float(re.search(r"^\$\d*,*\d*", listing.findNext(name="span").text)
                  .group()
                  .replace("$", "")
                  .replace(",", ""))
    return RentalListing(price=price, address=address, link=link)


def assure_element_visibility(locator, driver):
    wait = WebDriverWait(driver, WEBDRIVER_RENDER_TIMEOUT_SECONDS)
    return wait.until(ec.visibility_of_element_located(locator))


def write_to_spreadsheet(rental_listings: RentalListing):
    logging.info("Opening form...")
    driver = get_webdriver()
    driver.get(FORM_LOCATION)

    for index, rental_listing in enumerate(rental_listings):
        logging.info(f"Saving rental listing {index + 1}/{len(rental_listings)} to the form...")
        assure_element_visibility((By.XPATH, "//input[@type='text']"), driver)
        text_inputs = driver.find_elements(By.XPATH, "//input[@type='text']")

        [text_input.send_keys(text) for text_input, text in
         zip(text_inputs, [rental_listing.address, rental_listing.price, rental_listing.link])]

        driver.find_element(By.XPATH, "//span[text()='Enviar']").click()
        driver.find_element(By.XPATH, "//a[text()='Enviar outra resposta']").click()


def get_renting_website_data():
    soup = BeautifulSoup(requests.get(RENTING_WEBSITE_LOCATION).content, "html.parser")
    data = soup.find_all(class_=re.compile("ListItem"))
    logging.info(f"{len(data)} rental listings found")
    return data


def get_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    return webdriver.Chrome(options=options)


if __name__ == "__main__":
    main()
