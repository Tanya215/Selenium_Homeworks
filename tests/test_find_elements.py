from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_title(browser, url):
    browser.get(url)
    assert browser.title == "Your Store"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "search")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Featured']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-original-title"
                                                                                       "='Add to Wish List']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-original-title"
                                                                                       "='Compare this Product']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "logo")))


def test_catalog_title(browser, url):
    url_builder = f"{url}/desktops"
    browser.get(url_builder)
    assert browser.title == "Desktops"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "list-view")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "grid-view")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Product Compare (0)")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Sort By:']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Show:']")))


def test_product_card_title(browser, url):
    url_builder = f"{url}/macbook"
    browser.get(url_builder)
    assert browser.title == "MacBook"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@data-original-title='Add to Wish List']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@data-original-title='Compare this Product']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Qty']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "button-cart")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "quantity")))


def test_admin_page_title(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)
    assert browser.title == "Administration"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "OpenCart")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgotten Password")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()=' Please enter your login details.']")))


def test_register_page_title(browser, url):
    url_builder = f"{url}/index.php?route=account/register"
    browser.get(url_builder)
    assert browser.title == "Register Account"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Privacy Policy")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "login page")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='firstname']")))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "input-lastname")))
