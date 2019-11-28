from selenium import webdriver
import time
import pytest


@pytest.yield_fixture(scope="class")
def start_browser():
    baseURL = "https://invoice-mail.cisbox.com/admin/login"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseURL)
    yield driver
