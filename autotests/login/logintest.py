import unittest
from selenium import webdriver
from PageObjects.Login import Login


class SaucedemoLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.login_page = Login(self.driver)

    def test_login_valid_credentials(self):
        self.login_page.enter_username('standard_user')
        self.login_page.enter_password('secret_sauce')
        self.login_page.button_click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
