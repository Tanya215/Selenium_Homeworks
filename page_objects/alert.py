from selenium.webdriver.common.by import By


class Alert:

    def confirm_alert(self):
        confirm_alert = self.switch_to.alert
        confirm_alert.accept()

    def verify_success_product_update(self):
        self.find_element(By.CSS_SELECTOR, ".alert-success")

    def verify_success_customer_update(self):
        self.find_element(By.CSS_SELECTOR, ".alert-success")
