import os
import pytest
import allure

from datetime import datetime
from selenium.webdriver.common.by import By

from tests.base_test import BaseTest
from pages.login_page import LoginPageLocators, LoginPage
from pages.account_page import AccountPageLocators, AccountPage
from pages.transactions_page import TransactionsPageLocators, TransactionsPage


@pytest.mark.usefixtures("user_name")
class TestCustomerActions(BaseTest):
    @pytest.fixture(scope="session")
    def user_name(self):
        return os.environ.get("CUSTOMER_LOGIN")

    @pytest.fixture()
    def login_page(self, chrome_browser):
        return LoginPage(chrome_browser)

    @pytest.fixture()
    def account_page(self, chrome_browser):
        return AccountPage(chrome_browser)

    @pytest.fixture()
    def tx_page(self, chrome_browser):
        return TransactionsPage(chrome_browser)

    def collect_tx_table_data(self, tx_page):
        tx_table = []
        with open("reports/expected.csv", "w", encoding="utf-8") as out_file:
            for i in range(1, tx_page.count_tx_table_rows() + 1):
                d, a, t = [e.text for e in tx_page.get_row_n(i)]
                new_d = datetime.strptime(d, "%b %d, %Y %H:%M:%S %p").strftime(
                    "%d %B %Y %H:%M:%S"
                )
                out_file.write(f"{new_d} {a} {t} \n")
                tx_table.append([d, a, t])
        return tx_table

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Visit XYZ Bank site")
    @allure.label("Customer", "Harry")
    def test_visit_XYZ_Bank(self, login_page):
        login_page.open_page()
        assert login_page.get_title() == "XYZ Bank"

    @allure.title("Login as customer")
    @allure.label("Customer", "Harry")
    def test_login_as_customer(self, login_page, user_name):
        login_page.login_as_customer(user_name)
        assert login_page.find_element(LoginPageLocators.LOGOUT_BTN)

    @allure.title("Deposit money on account n check balance")
    @allure.label("Customer", "Harry")
    def test_deposit(self, login_page, account_page, user_name, fibonacci_n):
        login_page.login_as_customer(user_name)
        account_page.deposit(fibonacci_n)
        assert account_page.get_current_balance() == str(fibonacci_n)
        assert account_page.get_deposit_msg_text() == "Deposit Successful"

    @allure.title("Withdrawl money from account n check balance")
    @allure.label("Customer", "Harry")
    def test_withdrawl(self, login_page, account_page, user_name, fibonacci_n):
        login_page.login_as_customer(user_name)
        account_page.deposit(fibonacci_n)
        account_page.withdrawl(fibonacci_n)
        assert account_page.get_current_balance() == "0"
        assert account_page.get_withdrawl_msg_text() == "Transaction successful"

    @allure.title("Check transactions table, collect data")
    @allure.label("Customer", "Harry")
    def test_transactions(
        self, login_page, account_page, tx_page, user_name, fibonacci_n
    ):
        login_page.login_as_customer(user_name)
        account_page.deposit(fibonacci_n)
        account_page.withdrawl(fibonacci_n)
        account_page.click_transactions_btn()

        tx_table_data = self.collect_tx_table_data(tx_page)
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
