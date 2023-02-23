from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_field = (By.XPATH, '//*[@id="user-name"]')
        self.password_field = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH, '//*[@id="login-button"]')

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def button_click(self):
        self.wait.until(EC.visibility_of_element_located(self.login_button)).click()
