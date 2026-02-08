import time
from dotenv import load_dotenv
from selenium import webdriver
from src.test.constants.Constants import Constants
from src.test.pageObjects.idrive360.loginPage import LoginPage
from src.test.pageObjects.idrive360.dashBoardPage import DashboardPage
import os
from src.test.utils import *
import logging
from src.test.utils.logger_utils import get_logger
logger = get_logger(__name__)

logger.info("Starting positive case for Dashboard Page ")
def test_dashboard_idrive_positive(setup):
    driver = setup

    loginpage = LoginPage(driver)
    loginpage.login_to_idrive360(email=os.getenv("IDRIVE_USERNAME"),
                                 pwd = os.getenv("IDRIVE_PASSWORD"))

    dashboard_page = DashboardPage(driver)

    free_trial_text = dashboard_page.get_free_trial()
    assert free_trial_text == "Your free trial has expired"




