import time
from selenium.webdriver.common.by import By


class TransactionsPage:
    def __init__(self, driver):
        self.driver = driver

    def count_rows(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, "tbody tr"))

    def get_row_n(self, n):
        return self.driver.find_elements(By.CSS_SELECTOR, f"tbody tr:nth-child({n}) td")
