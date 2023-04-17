from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_title(browser, url):
    browser.get(url)
    assert browser.title == "Your Store"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "search")))


def test_catalog_title(browser, url):
    url_builder = f"{url}/desktops"
    browser.get(url_builder)
    assert browser.title == "Desktops"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "list-view")))


def test_product_card_title(browser, url):
    url_builder = f"{url}/macbook"
    browser.get(url_builder)
    assert browser.title == "MacBook"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@data-original-title='Add to Wish List']")))


def test_admin_page_title(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)
    assert browser.title == "Administration"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "OpenCart")))


def test_register_page_title(browser, url):
    url_builder = f"{url}/index.php?route=account/register"
    browser.get(url_builder)
    assert browser.title == "Register Account"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
