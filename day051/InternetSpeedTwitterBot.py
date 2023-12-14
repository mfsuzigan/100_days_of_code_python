from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

SPEED_TEST_URL = "https://www.speedtest.net/"
WEBDRIVER_RENDER_TIMEOUT_SECONDS = 60


class InternetSpeedTwitterBot:

    def __init__(self):
        self.up = 0
        self.down = 0
        self.driver = Chrome()

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        accept_terms_button = self.find_element_if_visible((By.ID, "onetrust-accept-btn-handler"))
        accept_terms_button.click()

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        self.find_element_if_visible((By.CLASS_NAME, "result-data"))

        self.down = self.driver.find_element(By.CLASS_NAME,
                                             "result-data-large.number.result-data-value.download-speed").text

        self.up = self.find_element_if_visible((By.CLASS_NAME,
                                                "result-data-large.number.result-data-value.upload-speed")).text

    def find_element_if_visible(self, locator):
        wait = WebDriverWait(self.driver, WEBDRIVER_RENDER_TIMEOUT_SECONDS)
        return wait.until(ec.visibility_of_element_located(locator))

    def tweet_at_provider(self):
        pass
