from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def check_by_name(self, name_text):
        return WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.NAME, name_text)))

    def check_by_xpath(self, xpath):
        self.find_element(By.XPATH, xpath)

    def check_by_css(self, css):
        return WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

    def check_by_id(self, id):
        return WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.ID, id)))

    def check_by_link(self, link_text):
        return WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
