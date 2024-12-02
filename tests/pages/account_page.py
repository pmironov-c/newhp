import time
from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def click_deposit_btn(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[ng-click="deposit()"]'
        ).click()
        time.sleep(1)

    def set_deposit_amount(self, amount):
        self.driver.find_element(By.TAG_NAME, "input").send_keys(amount)

    def click_deposit_submit_btn(self):
        self.driver.find_element(
            By.XPATH, '//button[@type="submit" and text()="Deposit"]'
        ).click()
        time.sleep(1)

    def deposit(self, amount):
        self.click_deposit_btn()
        self.set_deposit_amount(amount)
        self.click_deposit_submit_btn()

    def click_withdrawl_btn(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[ng-click="withdrawl()"]'
        ).click()
        time.sleep(1)

    def set_withdrawl_amount(self, amount):
        self.driver.find_element(By.TAG_NAME, "input").send_keys(amount)

    def click_withdrawl_submit_btn(self):
        self.driver.find_element(
            By.XPATH, '//button[@type="submit" and text()="Withdraw"]'
        ).click()
        time.sleep(1)

    def withdrawl(self, amount):
        self.click_withdrawl_btn()
        self.set_withdrawl_amount(amount)
        self.click_withdrawl_submit_btn()

    def click_transactions_btn(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[ng-click="transactions()"]'
        ).click()
        time.sleep(1)
