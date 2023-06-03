# add all setup here

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(r"C:\\chromedriver.exe"))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service("C:\\geckodriver.exe"))
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
