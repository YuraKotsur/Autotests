import unittest
from selenium import webdriver
from PageObjects.Login import Login


class SaucedemoLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.login_page = Login(self.driver)

    def test_login_valid_credentials(self):
        self.login_page.login('standard_user', 'secret_sauce')
        self.assertTrue(self.login_page.get_title().is_displayed())

    def test_login_invalid_credentials(self):
        self.login_page.login('standard_user', 'wrongpass')
        self.assertTrue(self.login_page.get_login_error().is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
