from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time
import unittest
class BookingAttractionsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    QUERY_INPUT = (By.NAME, "query")
    CALENDAR_DAY = (By.XPATH, "//td[@role='gridcell']//span[@data-date='{date}']")
    DATE_DIV = (By.CLASS_NAME, "css-tbiur0")
    CHECK_PRICES_BUTTON = (By.CSS_SELECTOR, "button[data-testid='search-button']")
    PARIS_IMAGE = (By.CSS_SELECTOR, "img[src='https://q-xx.bstatic.com/xdata/images/xphoto/533x300/72204347.jpg?k=2028e72e4ea4eb18da986b8a60fd841f65fe0575db5012d723233b4427939b4a&o=']")
    first_product_card = (By.XPATH, "//a[contains(text(), 'Обзорный круиз по городу')]")
    children_button_plus = (By.XPATH,"//button[@data-testid='select-ticket' and @type='submit' and contains(@class, 'a83ed08757')]")

    # Methods

    def check_warning(self):
        # Ожидание появления сообщения
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "a53cbfa6de"))
        )

        xpath_message_div = "//div[contains(@class, 'a53cbfa6de') and contains(@class, 'css-1jmzsfe') and contains(text(), 'Выберите хотя бы один билет для взрослого')]"

        # Ожидание появления элемента на странице
        message_div = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_message_div))
        )

    def first_product_card_click(self):
        first_product_card = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Обзорный круиз по городу')]")
        first_product_card.click()

    def switch_page(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
    def serf_page(self):

        self.driver.execute_script("window.scrollBy(0, window.innerHeight * 1.25);")
        time.sleep(3)

    def children_plus_button_click(self):
        buttonPlus = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "(//button[@class = 'a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a'])[3]"))
        )
        buttonPlus.click()

    def button_nxt_click(self):
        buttonNext = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[@data-testid='select-ticket' and @type='submit' and contains(@class, 'a83ed08757')]"))
        )
        buttonNext.click()
    def enter_query(self, query: str):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.QUERY_INPUT)
        )
        search_input.clear()
        search_input.send_keys(query)

    def select_date(self, date: str):
        """
        Select a date in the format 'YYYY-MM-DD' from the calendar.
        """
        day_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.CALENDAR_DAY[0], self.CALENDAR_DAY[1].format(date=date)))
        )
        day_element.click()

    def click_on_date_div(self):
        date_div_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DATE_DIV)
        )
        date_div_element.click()

    def click_on_check_prices_button(self):
        check_prices_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECK_PRICES_BUTTON)
        )
        check_prices_button_element.click()

    def click_on_paris_image(self):
        paris_image_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PARIS_IMAGE)
        )
        paris_image_element.click()
