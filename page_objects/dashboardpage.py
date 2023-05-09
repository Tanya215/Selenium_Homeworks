from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def product_list_open(self):
        self.find_element(By.XPATH, "//a[text()=' Catalog']").click()
        WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Products']"))).click()

    def customer_list_open(self):
        self.find_element(By.XPATH, "//a[text()=' Customers']").click()
        WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Customers']"))).click()
