import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_LOGIN_BTN = (By.XPATH, '//*[@ng-click="customer()"]')
    USER_SELECT_DD = (By.ID, "userSelect")

    def user_from_list_by_name(user):
        return (By.XPATH, f'//*[text()="{user}"]')

    LOGIN_BTN = (By.XPATH, '//button[@type="submit" and text()="Login"]')
    LOGOUT_BTN = (By.CSS_SELECTOR, "button.btn.logout")


class LoginPage(BasePage):
    @allure.step("Click 'Custome Login' button")
    def click_customer_login_btn(self):
        self.find_element(LoginPageLocators.CUSTOMER_LOGIN_BTN).click()

    @allure.step("Open dropdown with users")
    def click_user_select_dd(self):
        self.find_element(LoginPageLocators.USER_SELECT_DD).click()

    @allure.step("Select user from list")
    def select_user_from_list(self, user):
        self.find_element(LoginPageLocators.user_from_list_by_name(user)).click()

    @allure.step("Submit login")
    def click_login_btn(self):
        self.find_element(LoginPageLocators.LOGIN_BTN).click()
        self.wait_element(LoginPageLocators.LOGOUT_BTN)

    @allure.step("Login as customer")
    def login_as_customer(self, user_name):
        self.open_page()
        self.click_customer_login_btn()
        self.click_user_select_dd()
        self.select_user_from_list(user_name)
        self.click_login_btn()
