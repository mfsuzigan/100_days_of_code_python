import logging
from enum import Enum

from selenium.common import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from day051 import InternetProvider

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"
WEBDRIVER_RENDER_TIMEOUT_SECONDS = 60
MAX_OPERATION_ATTEMPTS = 5


class InternetSpeedTwitterBot:
    class PageLoadStrategy(Enum):
        EAGER = "eager"
        NORMAL = "normal"

    def __init__(self, internet_provider: InternetProvider, page_load_strategy: PageLoadStrategy = None):
        self.internet_provider = internet_provider

        self.upload_speed = -1
        self.download_speed = -1

        self.driver = self.get_web_driver(page_load_strategy)

    def get_web_driver(self, page_load_strategy: PageLoadStrategy = None):
        options = Options()
        options.page_load_strategy = page_load_strategy.value \
            if page_load_strategy else self.PageLoadStrategy.NORMAL.value
        return Chrome(options=options)

    def set_page_load_strategy(self, page_load_strategy):
        self.driver.quit()
        self.driver = self.get_web_driver(page_load_strategy=page_load_strategy)

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        self.accept_test_terms()

        logging.info("Starting test")
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        self.find_element_if_visible((By.CLASS_NAME, "result-data"))
        
        base_class_name = "result-data-large.number.result-data-value"
        self.download_speed = float(self.driver.find_element(By.CLASS_NAME, f"{base_class_name}.download-speed").text)
        self.upload_speed = float(self.driver.find_element(By.CLASS_NAME, f"{base_class_name}.upload-speed").text)

        logging.info(f"Test finished. Speeds (Mbps): download {self.download_speed}, upload: {self.upload_speed}")
        self.driver.quit()

    def accept_test_terms(self):
        attempts = 1
        accept_terms_button = self.find_element_if_visible((By.ID, "onetrust-accept-btn-handler"))

        while attempts <= MAX_OPERATION_ATTEMPTS:
            try:
                accept_terms_button.click()

            except (ElementClickInterceptedException, ElementNotInteractableException):
                logging.warning("Error accepting page terms, retrying")
                attempts += 1

    def find_element_if_visible(self, locator):
        wait = WebDriverWait(self.driver, WEBDRIVER_RENDER_TIMEOUT_SECONDS)
        return wait.until(ec.visibility_of_element_located(locator))

    def tweet_at_provider(self, username, password):
        test_has_been_conducted = self.download_speed > 0 and self.upload_speed > 0
        speeds_are_within_range = (self.upload_speed >= self.internet_provider.min_upload_speed and
                                   self.download_speed >= self.internet_provider.min_download_speed)

        if not test_has_been_conducted:
            logging.info("No test has been conducted, skipping tweet")

        elif speeds_are_within_range:
            logging.info("Download and upload speed within range, skipping tweet")

        else:
            logging.info("Logging in to Twitter")
            self.twitter_login(password, username)

            logging.info("Tweeeting to internet provider about internet speed")
            message = (f"[TEST] Hey {self.internet_provider.name}, why is my internet speed\n\n"
                       f"◦ download: {self.download_speed} Mbps\n"
                       f"◦ upload: {self.upload_speed} Mbps\n\n"
                       f"when I pay for {self.internet_provider.min_download_speed} download/"
                       f" {self.upload_speed} upload?")
            self.tweet_message(message)

        pass

    def twitter_login(self, password, username):
        self.driver.get(TWITTER_URL)
        sign_in_button = self.find_element_if_visible((By.XPATH,
                                                       "//*[@id='react-root']/div/div/div[2]/main/"
                                                       "div/div/div[1]/div/div/div[3]/div[5]/a/div"))
        sign_in_button.click()

        base_xpath = "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]"

        username_input = self.find_element_if_visible(
            (By.XPATH, f"{base_xpath}/div/div/div/div[5]/label/div/div[2]/div/input"))
        username_input.send_keys(username)

        next_button = self.find_element_if_visible((By.XPATH, f"{base_xpath}/div/div/div/div[6]/div"))
        next_button.click()

        password_input = self.find_element_if_visible(
            (By.XPATH, f"{base_xpath}/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
        password_input.send_keys(password)

        login_button = self.find_element_if_visible((By.XPATH, f"{base_xpath}/div[2]/div/div[1]/div/div/div/div"))
        login_button.click()

    def tweet_message(self, message):
        tweet_button = self.find_element_if_visible(
            (By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]"))
        tweet_button.click()

        base_xpath = ("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]"
                      "/div/div/div/div[3]/div[2]/div[1]/div/div/div")

        tweet_input = self.find_element_if_visible((By.XPATH,
                                                    f"{base_xpath}/div[1]/div[2]/div/div/div/div/div/div/div/div"
                                                    f"/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div"
                                                    f"/div/div"))
        tweet_input.send_keys(message)

        send_button = self.find_element_if_visible((By.XPATH, f"{base_xpath}/div[2]/div[2]/div/div/div/div[4]"))
        send_button.click()
