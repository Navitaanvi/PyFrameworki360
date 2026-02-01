import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(os.getenv("URL"))
    yield driver
    driver.quit()
