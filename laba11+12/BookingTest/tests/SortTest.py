import unittest
from selenium import webdriver
from pages.savedListPage import SavedListPage
from pages.SearchPage import SearchPage
from selenium.webdriver.common.action_chains import ActionChains
import time
class SortTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(SearchPage.PAGE_LINK)
        self.SearchPage = SearchPage(self.driver)
        self.saved_list = SavedListPage(self.driver)

    def test_sort_lowest(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        booking_automation = SearchPage(self.driver)
        booking_automation.set_min_slider_value(600)
        self.SearchPage.check_first_card_cost()

        self.SearchPage.click_sort_button()
        self.SearchPage.click_low_sort()

        self.SearchPage.check_first_card_cost()

    def test_sort_hiest(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        booking_automation = SearchPage(self.driver)
        booking_automation.set_min_slider_value(600)
        self.SearchPage.check_first_card_cost()

        self.SearchPage.click_sort_button()
        self.SearchPage.click_heigh_sort()

        self.SearchPage.check_first_card_cost()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)