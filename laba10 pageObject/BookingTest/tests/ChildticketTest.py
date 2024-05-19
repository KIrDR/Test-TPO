import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BookingAttractionsPage import BookingAttractionsPage

class TestBookingAttractions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.booking.com/attractions")
        self.driver.maximize_window()
        self.booking_page = BookingAttractionsPage(self.driver)

    def test_booking_attractions(self):
        # Клик по предопределенному Парижу
        self.booking_page.click_on_paris_image()

        # Ожидание загрузки страницы
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "css-1t4p5ju"))
        )

        self.booking_page.first_product_card_click()
        self.booking_page.switch_page()

        self.booking_page.serf_page()

        self.booking_page.children_plus_button_click()

        self.booking_page.button_nxt_click()
        self.booking_page.check_warning()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)