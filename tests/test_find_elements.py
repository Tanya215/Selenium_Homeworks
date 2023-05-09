from page_objects.basepage import BasePage


def test_main_page_title(browser, url):
    browser.get(url)

    assert browser.title == "Your Store"
    BasePage.check_by_name(browser, "search")
    BasePage.check_by_xpath(browser, "//h3[text()='Featured']")
    BasePage.check_by_css(browser, "button[data-original-title='Add to Wish List']")
    BasePage.check_by_css(browser, "button[data-original-title='Compare this Product']")
    BasePage.check_by_id(browser, "logo")


def test_catalog_title(browser, url):
    url_builder = f"{url}/desktops"
    browser.get(url_builder)
    assert browser.title == "Desktops"
    BasePage.check_by_id(browser, "list-view")
    BasePage.check_by_id(browser, "grid-view")
    BasePage.check_by_link(browser, "Product Compare (0)")
    BasePage.check_by_xpath(browser, "//label[text()='Sort By:']")
    BasePage.check_by_xpath(browser, "//label[text()='Show:']")


def test_product_card_title(browser, url):
    url_builder = f"{url}/macbook"
    browser.get(url_builder)
    assert browser.title == "MacBook"
    BasePage.check_by_xpath(browser, "//*[@data-original-title='Add to Wish List']")
    BasePage.check_by_xpath(browser, "//*[@data-original-title='Compare this Product']")
    BasePage.check_by_xpath(browser, "//label[text()='Qty']")
    BasePage.check_by_id(browser, "button-cart")
    BasePage.check_by_name(browser, "quantity")


def test_admin_page_title(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)
    assert browser.title == "Administration"
    BasePage.check_by_link(browser, "OpenCart")
    BasePage.check_by_link(browser, "Forgotten Password")
    BasePage.check_by_xpath(browser, "//label[text()='Username']")
    BasePage.check_by_xpath(browser, "//label[text()='Password']")
    BasePage.check_by_xpath(browser, "//h1[text()=' Please enter your login details.']")


def test_register_page_title(browser, url):
    url_builder = f"{url}/index.php?route=account/register"
    browser.get(url_builder)
    assert browser.title == "Register Account"
    BasePage.check_by_css(browser, "input[value='Continue']")
    BasePage.check_by_link(browser, "Privacy Policy")
    BasePage.check_by_link(browser, "login page")
    BasePage.check_by_css(browser, "input[name='firstname']")
    BasePage.check_by_id(browser, "input-lastname")
