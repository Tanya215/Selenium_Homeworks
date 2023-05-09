import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers_folder", default="/Users/tatyanakoryakovtseva/Downloads/drivers")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.0.103:8081")

@pytest.fixture()
def url(request):
    base_url = request.config.getoption("--base_url")
    yield base_url

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers_folder")
    headless: object = request.config.getoption("--headless")


    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        if headless:
            options.add_argument('--headless=new')
        service = ChromeService(executable_path=os.path.join(drivers_folder, "chromedriver"))
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(executable_path=os.path.join(drivers_folder, "geckodriver"), options=options)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "opera":
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Opera.app/Contents/MacOS/Opera"
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option('w3c', True)
        if headless:
            options.add_argument('--headless=new')
        service = ChromeService(OperaDriverManager().install())
        service.start()
        driver = webdriver.Remote(service.service_url, options=options)

    driver.maximize_window()

    yield driver

    driver.quit()
