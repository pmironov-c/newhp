from datetime import datetime
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage


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

    assert login_page.verify_successful_login()


def test_deposit(chrome_browser, fibonacci_n):
    user_name = "Harry Potter"
    amount = fibonacci_n
    login_page = LoginPage(chrome_browser)
    login_page.login_as_customer(user_name)

    account_page = AccountPage(chrome_browser)

    account_page.click_deposit_btn()
    account_page.set_deposit_amount(amount)
    account_page.click_deposit_submit_btn()

    assert chrome_browser.find_element(By.XPATH, '//*[text()="Deposit Successful"]')


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

    assert chrome_browser.find_element(By.XPATH, '//*[text()="Transaction successful"]')


def test_balance(chrome_browser, fibonacci_n):
    user_name = "Harry Potter"
    amount = fibonacci_n
    login_page = LoginPage(chrome_browser)
    login_page.login_as_customer(user_name)

    account_page = AccountPage(chrome_browser)
    account_page.deposit(amount)
    account_page.withdrawl(amount)

    es = chrome_browser.find_elements(By.CSS_SELECTOR, "div.center > strong")

    assert es[1].text == "0"


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

    assert tx_page.count_rows() == 2


