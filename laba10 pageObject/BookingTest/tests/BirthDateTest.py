import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage

class BirthDateTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.booking.com/index.html")
        self.main_page = MainPage(self.driver)

    def test_change_birth_date(self):
        self.main_page.click_sign_in_button()
        self.main_page.enter_email("testmail20005@gmail.com")
        self.main_page.click_continue_button()
        self.main_page.enter_password("kirillDRACH999")
        self.main_page.click_sign_in_submit_button()


        self.main_page.click_account_button()
        self.main_page.click_manage_account_button()
        self.main_page.click_personal_details_button()
        self.main_page.click_edit_birth_date_button()
        self.main_page.enter_birth_date("10", "Октябрь", "1899")
        self.main_page.click_save_birth_date_button()

        expected_error_message = "Укажите корректный год в четырехзначном формате"
        actual_error_message = self.main_page.get_birth_date_error_message()
        self.assertEqual(actual_error_message, expected_error_message, "Ошибка даты рождения не совпадает")



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
