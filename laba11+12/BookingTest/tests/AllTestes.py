import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from pages.savedListPage import SavedListPage
from pages.CarRetailPage import CarRetailPage
from pages.BookingAttractionsPage import BookingAttractionsPage

class AuthorizationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.booking.com/index.html")
        self.main_page = MainPage(self.driver)

    def test_sign_in(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        self.main_page.click_sign_in_button()
        self.main_page.enter_email("abracadabra999@gmail.com")
        self.main_page.click_continue_button()
        self.main_page.enter_password("P$Gj?9xXD5.rxtU")
        self.main_page.click_sign_in_submit_button()

        #expected_names = ["Your account", "Ваш аккаунт"]
        #actual_name = self.main_page.get_logged_in_user_name()
        #self.assertIn(actual_name, expected_names, "Имя пользователя не совпадает")

    def tearDown(self):
        self.driver.quit()

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

class TestBookingAttractions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.booking.com/attractions")
        self.driver.maximize_window()
        self.booking_page = BookingAttractionsPage(self.driver)

    def test_booking_attractions(self):
        self.booking_page.click_on_paris_image()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "css-1t4p5ju"))
        )

        self.booking_page.first_product_card_click()
        self.booking_page.switch_page()

        self.booking_page.serf_page()
        self.booking_page.children_plus_button_click()
        self.booking_page.button_nxt_click()

    def tearDown(self):
        self.driver.quit()

class MinimalCostTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(SearchPage.PAGE_LINK)
        self.SearchPage = SearchPage(self.driver)
        self.saved_list = SavedListPage(self.driver)

    def test_minimal_cost(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        booking_automation = SearchPage(self.driver)
        booking_automation.set_min_slider_value(600)
        self.SearchPage.check_first_card_cost()

    def tearDown(self):
        self.driver.quit()

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

    def test_sort_highest(self):
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

class SubscribeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.booking.com/index.html")
        self.main_page = MainPage(self.driver)


    def test_english_switch(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        self.main_page.switch_language_to_english()
        self.main_page.serf_page()

    def test_subscribe(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        self.main_page.switch_language_to_english()
        self.main_page.serf_page()
        self.main_page.serf_page()
        self.main_page.serf_page()
        self.main_page.send_email("testmailSuper@com")
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_by_offset(10, 10).click().perform()
        self.main_page.click_send_email()
        self.main_page.send_email("testmailSuper@gmail.com")
        self.main_page.click_send_email()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
