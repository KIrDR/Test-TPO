import unittest
from selenium import webdriver
from pages.MainPage import MainPage
from selenium.webdriver.common.action_chains import ActionChains
import time
class SubscribeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.booking.com/index.html")
        self.main_page = MainPage(self.driver)

    def test_subscribe(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        self.main_page.switch_language_to_english()
        self.main_page.serf_page()
        self.main_page.serf_page()
        self.main_page.serf_page()
        self.main_page.send_email("testmailSuper@com")
        self.main_page.click_send_email()
        self.main_page.send_email("testmailSuper@gmail.com")
        self.main_page.click_send_email()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()