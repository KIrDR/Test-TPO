import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.driver.get("https://www.booking.com/index.html")

    def test_sign_in(self):
        driver = self.driver


        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='header-sign-in-button']"))
        )
        sign_in_button.click()


        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
        )
        email_input.send_keys("pkkkk2004@gmail.com")


        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        continue_button.click()


        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        password_input.send_keys("kirillDRACH999")


        sign_in_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        sign_in_submit_button.click()


        expected_name = "Ваш аккаунт"
        name_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.a3332d346a.a6a383700c"))
        )
        actual_name = name_element.text
        self.assertEqual(actual_name, expected_name, "Имя пользователя не совпадает")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()