from page_objects.basepage import BasePage
from selenium.webdriver.common.by import By


class FirstPage(BasePage):

    def open_currency_dropdown(self):

        self.find_element(By.XPATH, "//span[text()='Currency']").click()

    def select_euro(self):
        self.find_element(By.CSS_SELECTOR, "button[name='EUR']").click()

    def check_selected_currency_euro(self):
        self.find_element(By.XPATH, "//strong[text()='€']")

    def select_pound(self):
        self.find_element(By.CSS_SELECTOR, "button[name='GBP']").click()

    def check_selected_currency_pound(self):
        self.find_element(By.XPATH, "//strong[text()='£']")

    def select_US_dollar(self):
        self.find_element(By.CSS_SELECTOR, "button[name='USD']").click()

    def check_selected_currency_US_dollar(self):
        self.find_element(By.XPATH, "//strong[text()='$']")

    def go_to_register(self):
        self.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.find_element(By.LINK_TEXT, "Register").click()
