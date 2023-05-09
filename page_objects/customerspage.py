from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.basepage import BasePage

class CustomersPage:

    def check_added_customer(self):
        WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.XPATH, "//td[text()='First_name Last_name']")))

    def select_customer(self):
        self.find_element(By.XPATH, "//td[text()='First_name Last_name']/../td/input").click()

    def delete_selected_customer(self):
        self.find_element(By.CSS_SELECTOR, "button[data-original-title='Delete']").click()
