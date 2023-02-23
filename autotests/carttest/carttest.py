import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class cart_test(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        login_field = driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    def cart_open(self):
        driver = self.driver
        cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()

    def test_add_to_cart(self):
        driver = self.driver
        self.login()
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(1)
        self.cart_open()
        time.sleep(1)
        cart_item = driver.find_element(By.CLASS_NAME, 'cart_item')
        self.assertTrue(cart_item.is_displayed())

    def test_review_correct_item_added_to_cart(self):
        self.login()
        driver = self.driver
        correct_item = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.cart_open()
        self.assertTrue(correct_item in driver.page_source)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
