from logging import exception
from selenium.webdriver.common.by import By
from src.test.utils.common_utils import webdriver_wait, webdriver_wait_clickable, webdriver_wait_presence
from src.test.utils.logger_utils import get_logger
logger = get_logger(__name__)

class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    user_logged_in = (By.XPATH,"(//a[contains(text(),'A')])[1]")
    free_trial = (By.XPATH,"(//span[normalize-space()='Your free trial has expired'])[1]")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def get_free_trial(self):
        return webdriver_wait(self.driver,DashboardPage.free_trial).text


