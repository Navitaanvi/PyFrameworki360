import pytest

from src.test.pageObjects.idrive360.loginPage import LoginPage
import os
from src.test.utils.utils import take_screenshot
from src.test.utils.logger_utils import get_logger
logger = get_logger(__name__)

logger.info("Starting Positive Login Test")
def test_idrive_positive(setup):
    driver = setup
    login_page =LoginPage(driver)
    login_page.login_to_idrive360(email = os.getenv("IDRIVE_USERNAME"),
                                  pwd = os.getenv("IDRIVE_PASSWORD")
                                  )


logger.info("Strating negative Login Test")
def test_idrive_neagtive(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_idrive360(email= os.getenv("IDRIVE_INVALID_USERNAME"),
                                  pwd = os.getenv("IDRIVE_INVALID_PASSWORD")
                                  )
    error_message_element_text = login_page.get_error_message()
    actual_text = error_message_element_text.text.strip()
    assert "incorrect" in actual_text.lower()
    take_screenshot(driver = driver, name = "test_idrive_negative")

from src.test.pageObjects.idrive360.loginPage import logger, LoginPage
from src.test.utils.excel_utils import read_excel

@pytest.mark.skip(reason = "Excel test disabled")
def test_idrive_login_using_excel(setup):
    logger.info("Starting Excel Driven Login Test")

    driver = setup
    login_page = LoginPage(driver)

    data = read_excel()

    for row in data:
        email = row["username"]
        pwd = row["password"]

        logger.info(f"Logging in with user: {email}")
        login_page.login_to_idrive360(email=email, pwd=pwd)

