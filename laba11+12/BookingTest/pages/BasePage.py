from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.booking.com"
        self.sing_in_link = (By.XPATH, "//a[@data-testid='header-sign-in-button']")


    def load(self):
        self.driver.get(self.url)

    def click_sing_in(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sing_in_link)).click()




