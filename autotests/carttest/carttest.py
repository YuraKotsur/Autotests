import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class cart_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        login_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        login_field.send_keys('standard_user')
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys("secret_sauce")
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        add_to_cart_button.click()
        time.sleep(1)
        cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]')
        cart.click()
        time.sleep(1)
        cart_item = driver.find_element(By.CLASS_NAME, 'cart_item')
        self.assertTrue(cart_item.is_displayed())




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
