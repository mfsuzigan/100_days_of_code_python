from selenium.common import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

SPEED_TEST_URL = "https://www.speedtest.net/"
WEBDRIVER_RENDER_TIMEOUT_SECONDS = 60
MAX_OPERATIONS_ATTEMPTS = 5


class InternetSpeedTwitterBot:

    def __init__(self):
        self.upload_speed = 0
        self.download_speed = 0
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = Chrome(options=options)

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        self.accept_terms()

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        self.find_element_if_visible((By.CLASS_NAME, "result-data"))
        self.download_speed = self.driver.find_element(By.CLASS_NAME,
                                                       "result-data-large.number.result-data-value.download-speed").text
        self.upload_speed = self.driver.find_element(By.CLASS_NAME,
                                                     "result-data-large.number.result-data-value.upload-speed").text

    def accept_terms(self):
        attempts = 1
        accept_terms_button = self.find_element_if_visible((By.ID, "onetrust-accept-btn-handler"))

        while attempts <= MAX_OPERATIONS_ATTEMPTS:
            try:
                accept_terms_button.click()

            except (ElementClickInterceptedException, ElementNotInteractableException):
                attempts += 1

    def find_element_if_visible(self, locator):
        wait = WebDriverWait(self.driver, WEBDRIVER_RENDER_TIMEOUT_SECONDS)
        return wait.until(ec.visibility_of_element_located(locator))

    def tweet_at_provider(self):
        pass
