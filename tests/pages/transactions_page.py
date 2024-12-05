import allure
from pages.base_page import BasePage
from pages.account_page import AccountPageLocators
from selenium.webdriver.common.by import By


class TransactionsPageLocators:
    TX_TABLE_ROWS = (By.CSS_SELECTOR, "tbody tr")
    BACK_BTN = (By.CSS_SELECTOR, 'button[ng-click="back()"]')

    def get_cells_from_row_n(n):
        return (By.CSS_SELECTOR, f"tbody tr:nth-child({n}) td")


class TransactionsPage(BasePage):
    @allure.step("COunt rows in table")
    def count_tx_table_rows(self):
        return len(self.find_elements(TransactionsPageLocators.TX_TABLE_ROWS))

    @allure.step("Collect data from row n")
    def get_row_n(self, n):
        return self.find_elements(TransactionsPageLocators.get_cells_from_row_n(n))

    @allure.step("Click 'Back' button")
    def click_back_button(self):
        self.find_element(TransactionsPageLocators.BACK_BTN).click()
        self.wait_element(AccountPageLocators.ACCOUNT_INFO)
