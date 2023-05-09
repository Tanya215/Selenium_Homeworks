from page_objects.firstpage import FirstPage


def test_change_currency(browser, url):
    browser.get(url)
    # select Euro
    FirstPage.open_currency_dropdown(browser)
    FirstPage.select_euro(browser)
    FirstPage.check_selected_currency_euro(browser)
    # select Pound
    FirstPage.open_currency_dropdown(browser)
    FirstPage.select_pound(browser)
    FirstPage.check_selected_currency_pound(browser)
    # select US dollar
    FirstPage.open_currency_dropdown(browser)
    FirstPage.select_US_dollar(browser)
    FirstPage.check_selected_currency_US_dollar(browser)