from page_objects.adminpage import AdminPage
from page_objects.dashboardpage import DashboardPage
from page_objects.productspage import ProductsPage
from page_objects.alert import Alert


def test_add_product(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)
    # Admin login
    AdminPage.login_to_admin(browser)
    # open product list
    DashboardPage.product_list_open(browser)
    # select product for deletion
    ProductsPage.select_product(browser)
    # delete product
    ProductsPage.delete_selected_product(browser)
    # click on alert
    Alert.confirm_alert(browser)
    # Verify alert
    Alert.verify_success_product_update(browser)

    