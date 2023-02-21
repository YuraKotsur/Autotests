import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SaucedemoLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_valid_credentials(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        login_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        login_field.send_keys('standard_user')
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys("secret_sauce")
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        time.sleep(2)
        title = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.assertTrue(title.is_displayed())

    def tearDown(self):
        self.driver.quit()

    def test_login_invalid_credentials(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        login_field = driver.find_element(By.ID, 'user-name')
        login_field.send_keys('invalid_user')
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys('invalid_password')
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, '//*[@data-test="error"]')
        self.assertTrue(error_message.is_displayed())


if __name__ == "__main__":
    unittest.main()
