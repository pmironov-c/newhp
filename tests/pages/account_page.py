from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountPageLocators:
    DEPOSIT_BTN = (By.CSS_SELECTOR, 'button[ng-click="deposit()"]')
    DEPOSIT_INPUT = (By.TAG_NAME, "input")
    DEPOSIT_MSG = (By.CSS_SELECTOR, "span.error")
    DEPOSIT_SUBMIT_BTN = (By.XPATH, '//button[@type="submit" and text()="Deposit"]')

    WITHDRAWL_BTN = (By.CSS_SELECTOR, 'button[ng-click="withdrawl()"]')
    WITHDRAWL_INPUT = (By.TAG_NAME, "input")
    WITHDRAWL_MSG = (By.CSS_SELECTOR, "span.error")
    WITHDRAWL_SUBMIT_BTN = (By.XPATH, '//button[@type="submit" and text()="Withdraw"]')

    TRANSACTIONS_BTN = (By.CSS_SELECTOR, 'button[ng-click="transactions()"]')
    TRANSACTIONS_TBL = (By.TAG_NAME, "table")

    ACCOUNT_INFO = (By.CSS_SELECTOR, "div.center > strong")


class AccountPage(BasePage):
    def click_deposit_btn(self):
        self.find_element(AccountPageLocators.DEPOSIT_BTN).click()
        self.wait_element(AccountPageLocators.DEPOSIT_SUBMIT_BTN)

    def set_deposit_amount(self, amount):
        self.find_element(AccountPageLocators.DEPOSIT_INPUT).send_keys(amount)

    def click_deposit_submit_btn(self):
        self.find_element(AccountPageLocators.DEPOSIT_SUBMIT_BTN).click()
        self.wait_element(AccountPageLocators.DEPOSIT_MSG)

    def deposit(self, amount):
        self.click_deposit_btn()
        self.set_deposit_amount(amount)
        self.click_deposit_submit_btn()

    def click_withdrawl_btn(self):
        self.find_element(AccountPageLocators.WITHDRAWL_BTN).click()
        self.wait_element(AccountPageLocators.WITHDRAWL_SUBMIT_BTN)

    def set_withdrawl_amount(self, amount):
        self.find_element(AccountPageLocators.WITHDRAWL_INPUT).send_keys(amount)

    def click_withdrawl_submit_btn(self):
        self.find_element(AccountPageLocators.WITHDRAWL_SUBMIT_BTN).click()
        self.wait_element(AccountPageLocators.WITHDRAWL_MSG)

    def withdrawl(self, amount):
        self.click_withdrawl_btn()
        self.set_withdrawl_amount(amount)
        self.click_withdrawl_submit_btn()

    def click_transactions_btn(self):
        self.find_element(AccountPageLocators.TRANSACTIONS_BTN).click()
        self.wait_element(AccountPageLocators.TRANSACTIONS_TBL)
