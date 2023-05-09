from page_objects.firstpage import FirstPage
from page_objects.registerpage import RegisterPage


def test_add_user(browser, url):
    browser.get(url)
    # open register form
    FirstPage.go_to_register(browser)
    # enter user data
    RegisterPage.enter_user_data(browser)
    # Submit user
    RegisterPage.submit_new_user(browser)
    # Verify user
    RegisterPage.verify_user_creation(browser)
