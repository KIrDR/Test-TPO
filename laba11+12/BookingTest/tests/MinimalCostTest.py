import unittest
from selenium import webdriver
from pages.savedListPage import SavedListPage
from pages.SearchPage import SearchPage
from selenium.webdriver.common.action_chains import ActionChains
import time
class MinimalCostTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(SearchPage.PAGE_LINK)
        self.SearchPage = SearchPage(self.driver)
        self.saved_list = SavedListPage(self.driver)



    def test_minimal_cost(self):
        booking_automation = SearchPage(self.driver)
        booking_automation.set_min_slider_value(600)
        self.SearchPage.check_first_card_cost()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)