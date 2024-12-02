from datetime import datetime
import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage


def test_grab_transactions_data_in_file(chrome_browser, fibonacci_n):
    user_name = "Harry Potter"
    amount = fibonacci_n
    login_page = LoginPage(chrome_browser)
    login_page.login_as_customer(user_name)

    account_page = AccountPage(chrome_browser)
    account_page.deposit(amount)
    account_page.withdrawl(amount)
    account_page.click_transactions_btn()

    tx_page = TransactionsPage(chrome_browser)

    with open("tests/expected.csv", "w", encoding="utf-8") as out_file:
        for i in range(1, tx_page.count_rows() + 1):
            d, a, t = [e.text for e in tx_page.get_row_n(i)]
            new_d = datetime.strptime(d, "%b %d, %Y %H:%M:%S %p").strftime(
                "%d %B %Y %H:%M:%S"
            )
            out_file.write(f"{new_d} {a} {t} \n")

    allure.attach.file("tests/expected.csv", "Transactions data")
    assert tx_page.count_rows() == 2
