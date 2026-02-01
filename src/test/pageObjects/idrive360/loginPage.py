from logging import exception

from selenium.webdriver.common.by import By
from src.test.utils.common_utils import webdriver_wait, webdriver_wait_clickable, webdriver_wait_presence


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    user_email = (By.ID,"username")
    password = (By.NAME,"password")
    sign_in_button = (By.ID,"frm-btn")
    error_message = (By.XPATH,"//app-toast-message//p[contains(text(),'incorrect')]")

    def get_user_email(self):
        return webdriver_wait(self.driver,LoginPage.user_email)

    def get_password(self):
        return webdriver_wait(self.driver, LoginPage.password)

    def get_sign_in_button(self):
        return webdriver_wait_clickable(self.driver,LoginPage.sign_in_button)

    def get_error_message(self):
        return webdriver_wait_presence(self.driver,LoginPage.error_message)

    def login_to_idrive360(self,email,pwd):
        try:
            self.get_user_email().send_keys(email)
            self.get_password().send_keys(pwd)
            self.get_sign_in_button().click()

        except exception as e:
            print(e)
