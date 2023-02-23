import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Login import Login


class SaucedemoLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.login_page = Login(self.driver)

    def test_login_valid_credentials(self):
        driver = self.driver
        self.login_page.login('standard_user', 'secret_sauce')
        title = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.assertTrue(title.is_displayed())

    def test_login_invalid_credentials(self):
        self.login_page.login('standard_user', 'wrongpass')
        error = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertTrue(error.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
