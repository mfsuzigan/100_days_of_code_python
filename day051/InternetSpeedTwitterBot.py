import logging
from enum import Enum

from selenium.common import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"
WEBDRIVER_RENDER_TIMEOUT_SECONDS = 60
MAX_OPERATIONS_ATTEMPTS = 5


class InternetSpeedTwitterBot:
    class PageLoadStrategy(Enum):
        EAGER = "eager"
        NORMAL = "normal"

    def __init__(self, page_load_strategy: PageLoadStrategy = None):
        self.upload_speed = 0
        self.download_speed = 0
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

        self.accept_terms()

        logging.info("Starting test")
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        self.find_element_if_visible((By.CLASS_NAME, "result-data"))
        self.download_speed = self.driver.find_element(By.CLASS_NAME,
                                                       "result-data-large.number.result-data-value.download-speed").text
        self.upload_speed = self.driver.find_element(By.CLASS_NAME,
                                                     "result-data-large.number.result-data-value.upload-speed").text

        logging.info(f"Test finished. Speeds (Mbps): download {self.download_speed}, upload: {self.upload_speed}")
        self.driver.quit()

    def accept_terms(self):
        attempts = 1
        accept_terms_button = self.find_element_if_visible((By.ID, "onetrust-accept-btn-handler"))

        while attempts <= MAX_OPERATIONS_ATTEMPTS:
            try:
                accept_terms_button.click()

            except (ElementClickInterceptedException, ElementNotInteractableException):
                logging.warning("Error accepting page terms, retrying")
                attempts += 1

    def find_element_if_visible(self, locator):
        wait = WebDriverWait(self.driver, WEBDRIVER_RENDER_TIMEOUT_SECONDS)
        return wait.until(ec.visibility_of_element_located(locator))

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sign_in_button = self.find_element_if_visible((By.XPATH,
                                                       "//*[@id='react-root']/div/div/div[2]/main/"
                                                       "div/div/div[1]/div/div/div[3]/div[5]/a/div"))
        sign_in_button.click()
        username_input = self.find_element_if_visible((By.XPATH,
                                                       "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"))

        username_input.send_keys("USERNAME")
        next_button = self.find_element_if_visible((By.XPATH,
                                                    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"))
        next_button.click()
        password_input = self.find_element_if_visible((By.XPATH,
                                                       "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
        password_input.send_keys("PASSWORD")

        login_button = self.find_element_if_visible((By.XPATH,
                                                     "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"))
        login_button.click()
        pass
