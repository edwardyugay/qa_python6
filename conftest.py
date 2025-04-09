import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.headless = False  # Измените на True, если требуется headless-режим
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
