from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        self.username_field = (By.XPATH, '//*[@id="user-name"]')
        self.password_field = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH, '//*[@id="login-button"]')
        self.title = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.login_error = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.login_button)).click()

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.title))

    def get_login_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.login_error))