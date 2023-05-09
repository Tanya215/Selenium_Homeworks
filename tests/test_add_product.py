from page_objects.adminpage import AdminPage
from page_objects.dashboardpage import DashboardPage
from page_objects.productspage import ProductsPage
from page_objects.alert import Alert
import time


def test_add_product(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)
    # admin login
    AdminPage.login_to_admin(browser)
    # product list open
    DashboardPage.product_list_open(browser)
    # add a product
    ProductsPage.add_new_product(browser)
    # check added product
    ProductsPage.check_added_product(browser)
    # check alert
    Alert.verify_success_product_update(browser)

