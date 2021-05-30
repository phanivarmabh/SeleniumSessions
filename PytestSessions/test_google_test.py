from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")


def teardown_module(module):
    time.sleep(2)
    driver.quit()


def test_google_title():
    assert driver.title == 'Google'


def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"

