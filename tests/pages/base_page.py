from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotInteractableException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(
        self, url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#"
    ):
        return self.driver.get(url)

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def wait_element(self, locator, explicit_timeout=5):
        errors = [NoSuchElementException, ElementNotInteractableException]
        WebDriverWait(
            self.driver,
            timeout=explicit_timeout,
            poll_frequency=0.2,
            ignored_exceptions=errors,
        ).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def get_title(self):
        return self.driver.title
