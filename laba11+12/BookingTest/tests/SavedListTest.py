import unittest
from selenium import webdriver
from pages.savedListPage import SavedListPage
from pages.MainPage import MainPage
from selenium.webdriver.common.action_chains import ActionChains
import time
class SavedListTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://booking.com/mywishlist.html?wl=aezNRKWsExzPTgP8kmcHU2MGcdA")
        self.main_page = MainPage(self.driver)
        self.saved_list = SavedListPage(self.driver)

    def test_subscribe(self):
        self.saved_list.check_name()
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()