from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.test.constants import Constants

def webdriver_wait(driver,element_tuple,timeout=15):
    return WebDriverWait(driver,timeout).until(
        EC.visibility_of_element_located(element_tuple)
    )

def webdriver_wait_clickable(driver, element_tuple, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(element_tuple)
    )

def webdriver_wait_presence(driver, element_tuple, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(element_tuple)
    )

def webdriver_wait_url(driver,timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.url_changes(Constants.app_dashboard_url)
    )
