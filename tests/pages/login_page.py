import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_customer_login_btn(self):
        self.driver.find_element(By.XPATH, '//*[@ng-click="customer()"]').click()

    def click_user_select_dd(self):
        self.driver.find_element(By.ID, "userSelect").click()

    def select_user_from_list(self, user):
        self.driver.find_element(By.XPATH, f'//*[text()="{user}"]').click()

    def click_login_btn(self):
        self.driver.find_element(
            By.XPATH, '//button[@type="submit" and text()="Login"]'
        ).click()

    def verify_successful_login(self):
        try:
            time.sleep(2)
            logout_btn = self.driver.find_element(By.CSS_SELECTOR, "button.btn.logout")
            return logout_btn.is_displayed()
        except NoSuchElementException:
            assert False, "Logout button does not exist."

    def login_as_customer(self, user_name):
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
        self.open_page(url)

        self.click_user_select_dd()
        self.select_user_from_list(user_name)
        self.click_login_btn()
