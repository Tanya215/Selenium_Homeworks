from page_objects.adminpage import AdminPage
from page_objects.dashboardpage import DashboardPage
from page_objects.customerspage import CustomersPage
from page_objects.alert import Alert


def test_delete_user(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)
    # Admin login
    AdminPage.login_to_admin(browser)
    # Open customers list
    DashboardPage.customer_list_open(browser)
    # check that customer was added
    CustomersPage.check_added_customer(browser)
    # Select the customer
    CustomersPage.select_customer(browser)
    # Delete the customer
    CustomersPage.delete_selected_customer(browser)
    # Confirm deletion
    Alert.confirm_alert(browser)
    # Verify alert
    Alert.verify_success_customer_update(browser)
