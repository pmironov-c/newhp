from datetime import datetime
from selenium.webdriver.common.by import By
from pages.login_page import LoginPageLocators, LoginPage
from pages.account_page import AccountPageLocators, AccountPage
from pages.transactions_page import TransactionsPageLocators, TransactionsPage


def test_visit_XYZ_Bank(chrome_browser):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#"
    login_page = LoginPage(chrome_browser)

    login_page.open_page(url)
    assert chrome_browser.title == "XYZ Bank"


def test_login_as_HP(chrome_browser):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    user_name = "Harry Potter"
    login_page = LoginPage(chrome_browser)

    login_page.open_page(url)

    login_page.click_customer_login_btn()
    login_page.click_user_select_dd()
    login_page.select_user_from_list(user_name)
    login_page.click_login_btn()

    assert login_page.find_element(LoginPageLocators.LOGOUT_BTN)


def test_deposit(chrome_browser, fibonacci_n):
    user_name = "Harry Potter"
    amount = fibonacci_n
    login_page = LoginPage(chrome_browser)
    login_page.login_as_customer(user_name)

    account_page = AccountPage(chrome_browser)

    account_page.click_deposit_btn()
    account_page.set_deposit_amount(amount)
    account_page.click_deposit_submit_btn()

    assert account_page.find_elements(AccountPageLocators.ACCOUNT_INFO)[1].text == str(
        amount
    )
    assert (
        account_page.find_element(AccountPageLocators.DEPOSIT_MSG).text
        == "Deposit Successful"
    )


def test_withdrawl(chrome_browser, fibonacci_n):
    user_name = "Harry Potter"
    amount = fibonacci_n
    login_page = LoginPage(chrome_browser)
    login_page.login_as_customer(user_name)

    account_page = AccountPage(chrome_browser)
    account_page.deposit(amount)

    account_page.click_withdrawl_btn()
    account_page.set_withdrawl_amount(amount)
    account_page.click_withdrawl_submit_btn()

    assert (
        account_page.find_element(AccountPageLocators.WITHDRAWL_MSG).text
        == "Transaction successful"
    )


def test_balance(chrome_browser, fibonacci_n):
    user_name = "Harry Potter"
    amount = fibonacci_n
    login_page = LoginPage(chrome_browser)
    login_page.login_as_customer(user_name)

    account_page = AccountPage(chrome_browser)
    account_page.deposit(amount)
    account_page.withdrawl(amount)

    assert account_page.find_elements(AccountPageLocators.ACCOUNT_INFO)[1].text == "0"


def test_transactions(chrome_browser, fibonacci_n):
    user_name = "Harry Potter"
    amount = fibonacci_n
    login_page = LoginPage(chrome_browser)
    login_page.login_as_customer(user_name)

    account_page = AccountPage(chrome_browser)
    account_page.deposit(amount)
    account_page.withdrawl(amount)

    account_page.click_transactions_btn()
    tx_page = TransactionsPage(chrome_browser)

    err = []
    if tx_page.count_tx_table_rows() != 2:
        err.append(f"Should be 2 rows in table")
    if tx_page.get_row_n(1)[1].text != str(amount) != tx_page.get_row_n(1)[1].text:
        err.append(f"Amount in 1st and 2nd rows should be equal to {amount}")
    if tx_page.get_row_n(1)[2].text != "Credit":
        err.append(f"Transaction type in 1st row should be 'Credit'")
    if tx_page.get_row_n(2)[2].text != "Debit":
        err.append(f"Transaction type in 2nd row should be 'Debit'")

    assert not err, f"errors occured:\n{"\n".join(err)}"
