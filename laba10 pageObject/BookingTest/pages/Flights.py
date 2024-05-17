from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FlightsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.booking.com/flights/index.html"
        self.flight_from = (By.XPATH, "//button[@data-ui-name='input_location_from_segment_0']")
        self.flight_from_input = (By.XPATH, "//input[@data-ui-name='input_text_autocomplete' and @aria-expanded='false']")
        self.flight_in = (By.XPATH, "//button[@class='ShellButton-module__btn___tCJzz']")
        self.flight_in_input = (By.XPATH, "//input[@data-ui-name='input_text_autocomplete' and @aria-expanded='true']")
        self.calendar_button = (By.XPATH, "//button[contains(@class, 'ShellButton-module__btn___tCJzz')]")
        self.search_button = (By.XPATH, '//button[@data-ui-name="button_search_submit"]')


    def load(self):
        self.driver.get(self.url)


    def click_flight_from(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.flight_from)).click()

    def click_flight_in(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.flight_in)).click()

    def click_calendar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.calendar_button)).click()

    def click_date_from_calendar(self, date_from):
        self.click_calendar(self)
        data_ui_name = '//span[@data-ui-name="calendar_cell_2024-06-' + date_from + '"]//span[text()="' + date_from + '"]'
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, data_ui_name)).click()

    def click_date_to_calendar(self, date_to):
        self.click_calendar(self)
        data_ui_name = '//span[@data-ui-name="calendar_cell_2024-07-' + date_to + '"]//span[text()="' + date_to + '"]'
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, data_ui_name)).click()

    def click_search(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()

    def enter_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
