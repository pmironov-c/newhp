import os
import subprocess
from datetime import datetime

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
@allure.title("Chrome browser")
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.timeouts = {"pageLoad": 5 * 10e3, "script": 5 * 10e3, "implicit": 5 * 10e3}
    options.page_load_strategy = "normal"

    options.add_argument("--start-maximized --auto-open-devtools-for-tabs")
    options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub", options=options
    )

    yield driver
    driver.quit()


@pytest.fixture()
def fibonacci_n():
    n = datetime.now().day + 1

    def fibonacci(n):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 2) + fibonacci(n - 1)

    yield fibonacci(n)
