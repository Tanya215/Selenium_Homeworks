from selenium.webdriver.common.by import By
import datetime


class RegisterPage:

    def enter_user_data(self):
        self.find_element(By.ID, "input-firstname").send_keys("First_name")
        self.find_element(By.ID, "input-lastname").send_keys("Last_name")
        current_time = datetime.datetime.now()
        email = datetime.datetime.strftime(current_time, '%f') + '@gmail.com'
        self.find_element(By.ID, "input-email").send_keys(email)
        self.find_element(By.ID, "input-telephone").send_keys("1231231231")
        self.find_element(By.ID, "input-password").send_keys("Test1234")
        self.find_element(By.ID, "input-confirm").send_keys("Test1234")
        self.find_element(By.CSS_SELECTOR, "input[name='agree']").click()

    def submit_new_user(self):
        self.find_element(By.CSS_SELECTOR, "input[value='Continue']").click()

    def verify_user_creation(self):
        self.find_element(By.XPATH, "//h1[text()='Your Account Has Been Created!']")
        