import os
import pytest
import allure

from datetime import datetime
from selenium.webdriver.common.by import By

from base_test import BaseTest
from pages.login_page import LoginPageLocators as login_locators, LoginPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage


class TestCustomerActions(BaseTest):
    @pytest.fixture(autouse=True)
    @classmethod
    def pages_init(cls, chrome_browser):
        cls.login_page = LoginPage(chrome_browser)
        cls.account_page = AccountPage(chrome_browser)
        cls.tx_page = TransactionsPage(chrome_browser)

    def collect_tx_table_data(self):
        tx_table = []
        with open("reports/expected.csv", "w", encoding="utf-8") as out_file:
            for i in range(1, self.tx_page.count_tx_table_rows() + 1):
                d, a, t = [e.text for e in self.tx_page.get_row_n(i)]
                new_d = datetime.strptime(d, "%b %d, %Y %H:%M:%S %p").strftime(
                    "%d %B %Y %H:%M:%S"
                )
                out_file.write(f"{new_d} {a} {t} \n")
                tx_table.append([d, a, t])
        return tx_table

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Visit XYZ Bank site")
    @allure.label("Customer", "Harry")
    def test_visit_XYZ_Bank(self):
        self.login_page.open_page()
        assert self.login_page.get_title() == "XYZ Bank"

    @allure.title("Login as customer")
    @allure.label("Customer", "Harry")
    def test_login_as_customer(self):
        self.login_page.login_as_customer(self.user_name)
        assert self.login_page.find_element(login_locators.LOGOUT_BTN)

    @allure.title("Deposit money on account n check balance")
    @allure.label("Customer", "Harry")
    def test_deposit(self, fibonacci_n):
        self.login_page.login_as_customer(self.user_name)
        self.account_page.deposit(fibonacci_n)
        assert self.account_page.get_current_balance() == str(fibonacci_n)
        assert self.account_page.get_deposit_msg_text() == "Deposit Successful"

    @allure.title("Withdrawl money from account n check balance")
    @allure.label("Customer", "Harry")
    def test_withdrawl(self, fibonacci_n):
        self.login_page.login_as_customer(self.user_name)
        self.account_page.deposit(fibonacci_n)
        self.account_page.withdrawl(fibonacci_n)
        assert self.account_page.get_current_balance() == "0"
        assert self.account_page.get_withdrawl_msg_text() == "Transaction successful"

    @allure.title("Check transactions table, collect data")
    @allure.label("Customer", "Harry")
    def test_transactions(self, fibonacci_n):
        self.login_page.login_as_customer(self.user_name)
        self.account_page.deposit(fibonacci_n)
        self.account_page.withdrawl(fibonacci_n)
        self.account_page.click_transactions_btn()

        tx_table_data = self.collect_tx_table_data()
        allure.attach.file("reports/expected.csv", "Transactions data")

        e = []
        if len(tx_table_data) != 2:
            e.append(f"Should be 2 rows in table")
        if tx_table_data[0][1] != str(fibonacci_n) != tx_table_data[1][1]:
            e.append(f"Amount in 1st and 2nd rows should be equal to {fibonacci_n}")
        if tx_table_data[0][2] != "Credit":
            e.append(f"Transaction type in 1st row should be 'Credit'")
        if tx_table_data[1][2] != "Debit":
            e.append(f"Transaction type in 2nd row should be 'Debit'")

        assert not e, f"errors occured:\n{"\n".join(e)}"
