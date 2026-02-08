from logging import exception
from selenium.webdriver.common.by import By
from src.test.utils.common_utils import webdriver_wait, webdriver_wait_clickable, webdriver_wait_presence
from src.test.utils.logger_utils import get_logger
logger = get_logger(__name__)

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
            logger.info("Entering email")
            email_field = self.get_user_email()
            email_field.clear()
            email_field.send_keys(email)

            logger.info("Entering Password")
            password_field = self.get_password()
            password_field.clear()
            password_field.send_keys(pwd)

            logger.debug("Locating Sign In button")
            try:
                btn = self.get_sign_in_button()

                if btn.is_enabled():
                    logger.info("Sign In button is enabled — clicking")
                    btn.click()
                else:
                    logger.warning("Sign In button found but is disabled")

            except Exception as e:
                logger.critical(f"Sign In button could not be clicked: {e}", exc_info=True)
                raise

            self.get_sign_in_button().click()

        except exception as e:
            print(e)
