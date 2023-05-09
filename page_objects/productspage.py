from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def add_new_product(self):
        self.find_element(By.CSS_SELECTOR, "a[data-original-title='Add New']").click()
        self.find_element(By.ID, "input-name1").send_keys("1Product_test")
        self.find_element(By.ID, "input-meta-title1").send_keys("Product_meta_tag")
        self.find_element(By.LINK_TEXT, "Data").click()
        self.find_element(By.ID, "input-model").send_keys("Product_model")
        self.find_element(By.CSS_SELECTOR, "button[data-original-title='Save']").click()

    def check_added_product(self):
        WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.XPATH, "//td[text()='1Product_test']")))

    def select_product(self):
        self.find_element(By.XPATH, "//td[text()='1Product_test']/../td/input").click()

    def delete_selected_product(self):
        self.find_element(By.CSS_SELECTOR, "button[data-original-title='Delete']").click()
