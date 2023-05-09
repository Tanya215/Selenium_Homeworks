from selenium.webdriver.common.by import By


class AdminPage:

    def login_to_admin(self):
        self.find_element(By.ID, "input-username").send_keys("user")
        self.find_element(By.ID, "input-password").send_keys("bitnami")
        self.find_element(By.XPATH, "//button[text()=' Login']").click()
