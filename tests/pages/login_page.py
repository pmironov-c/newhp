from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPageLocators:
    customer_login_btn = (By.XPATH, '//*[@ng-click="customer()"]')
    user_select_dropdown = (By.ID, "userSelect")

    def user_from_list_by_name(user):
        return (By.XPATH, f'//*[text()="{user}"]')

    login_btn = (By.XPATH, '//button[@type="submit" and text()="Login"]')
    logout_btn = (By.CSS_SELECTOR, "button.btn.logout")


class LoginPage(BasePage):
    def click_customer_login_btn(self):
        self.find_element(LoginPageLocators.customer_login_btn).click()

    def click_user_select_dd(self):
        self.find_element(LoginPageLocators.user_select_dropdown).click()

    def select_user_from_list(self, user):
        self.find_element(LoginPageLocators.user_from_list_by_name(user)).click()

    def click_login_btn(self):
        self.find_element(LoginPageLocators.login_btn).click()
        self.wait_element(LoginPageLocators.logout_btn)

    def login_as_customer(self, user_name):
        self.open_page()
        self.click_user_select_dd()
        self.select_user_from_list(user_name)
        self.click_login_btn()
