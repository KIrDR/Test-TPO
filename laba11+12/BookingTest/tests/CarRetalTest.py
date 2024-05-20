import unittest
from selenium import webdriver
from pages.savedListPage import SavedListPage
from pages.SearchPage import SearchPage
from pages.CarRetailPage import CarRetailPage
from selenium.webdriver.common.action_chains import ActionChains
import time
class CarRetailTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.SearchPage = SearchPage(self.driver)
        self.saved_list = SavedListPage(self.driver)
        self.CarRetailPage = CarRetailPage(self.driver)
        self.driver.get(self.CarRetailPage.carRetailLink)


    def test_same_date(self):
        self.CarRetailPage.drop_off_date_click()

        self.CarRetailPage.click_date_span()
        self.CarRetailPage.click_search_button()
        self.CarRetailPage.check_error_message_filled()



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)