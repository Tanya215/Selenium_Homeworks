import requests
from http import HTTPStatus
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_title(browser, url):
    browser.get(url)
    url_link = requests.get(url)
    assert url_link.status_code == HTTPStatus.OK
    assert browser.title == "Your Store"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "search")))


def test_catalog_title(browser, url):
    url_builder = f"{url}/desktops"
    url_link = requests.get(url_builder)
    browser.get(url_builder)
    assert url_link.status_code == HTTPStatus.OK
    assert browser.title == "Desktops"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "list-view")))


def test_product_card_title(browser, url):
    url_builder = f"{url}/macbook"
    url_link = requests.get(url_builder)
    browser.get(url_builder)
    assert url_link.status_code == HTTPStatus.OK
    assert browser.title == "MacBook"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@data-original-title='Add to Wish List']")))


def test_admin_page_title(browser, url):
    url_builder = f"{url}/admin"
    url_link = requests.get(url_builder)
    browser.get(url_builder)
    assert url_link.status_code == HTTPStatus.OK
    assert browser.title == "Administration"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "OpenCart")))


def test_register_page_title(browser, url):
    url_builder = f"{url}/index.php?route=account/register"
    url_link = requests.get(url_builder)
    browser.get(url_builder)
    assert url_link.status_code == HTTPStatus.OK
    assert browser.title == "Register Account"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
