import unittest
from selenium import webdriver
from pages.MainPage import MainPage

class AuthorizationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.booking.com/index.html")
        self.main_page = MainPage(self.driver)

    def test_sign_in(self):
        self.main_page.click_sign_in_button()
        self.main_page.enter_email("testmail20005@gmail.com")
        self.main_page.click_continue_button()
        self.main_page.enter_password("kirillDRACH999")
        self.main_page.click_sign_in_submit_button()

        expected_names = ["Your account", "Ваш аккаунт"]
        actual_name = self.main_page.get_logged_in_user_name()
        self.assertIn(actual_name, expected_names, "Имя пользователя не совпадает")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
