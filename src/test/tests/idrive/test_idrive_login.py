from src.test.pageObjects.idrive360.loginPage import LoginPage
import os
from src.test.utils.utils import take_screenshot

def test_idrive_positive(setup):
    driver = setup
    login_page =LoginPage(driver)
    login_page.login_to_idrive360(email = os.getenv("USERNAME"),
                                  pwd = os.getenv("PASSWORD")
                                  )

def test_idrive_neagtive(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_idrive360(email= os.getenv("INVALID_USERNAME"),
                                  pwd = os.getenv("INVALID_PASSWORD")
                                  )
    error_message_element_text = login_page.get_error_message()
    actual_text = error_message_element_text.text.strip()
    assert "incorrect" in actual_text.lower()
    take_screenshot(driver = driver, name = "test_idrive_negative")







