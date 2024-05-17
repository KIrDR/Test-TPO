from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class StaysPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.booking.com"
        self.input_to = (By.XPATH, "//input[@data-testid='destination-container']/input[@placeholder='Куда вы хотите поехать?']")
        self.calendar_button = (By.XPATH, "//span[contains(@class, 'date-display-field-start')]/preceding-sibling::button")
        self.search_button = (By.XPATH, "//button[@class='a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b']")

    def load(self):
        self.driver.get(self.url)

    def enter_destination(self, destination):
        self._clear_input(self.input_to)
        self._enter_text(self.input_to, destination)

    def click_calendar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.calendar_button)).click()

    def click_search(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button)).click()

    def _clear_input(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()

    def _enter_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
