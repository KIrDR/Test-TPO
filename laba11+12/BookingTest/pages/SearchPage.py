from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    QUERY_INPUT = (By.NAME, "query")
    CALENDAR_DAY = (By.XPATH, "//td[@role='gridcell']//span[@data-date='{date}']")
    DATE_DIV = (By.CLASS_NAME, "css-tbiur0")
    CHECK_PRICES_BUTTON = (By.CSS_SELECTOR, "button[data-testid='search-button']")
    PARIS_IMAGE = (By.CSS_SELECTOR,"img[src='https://q-xx.bstatic.com/xdata/images/xphoto/533x300/72204347.jpg?k=2028e72e4ea4eb18da986b8a60fd841f65fe0575db5012d723233b4427939b4a&o=']")
    PAGE_LINK = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaCWIAQGYATG4ARfIAQzYAQHoAQH4AQmIAgGoAgO4AvGwrrIGwAIB0gIkYzRiNjdjOTgtODkyOC00M2ZjLWFkNjgtMmU3NjhhNjVmMDZl2AIG4AIB&sid=805285a7efe5a73126f1e429455e96f1&aid=304142&ss=Paris&ssne=Paris&ssne_untouched=Paris&efdco=1&lang=en-us&src=searchresults&dest_id=-1456928&dest_type=city&checkin=2024-07-17&checkout=2024-07-18&group_adults=2&no_rooms=1&group_children=0&nflt=price%3DBYN-800-max-1"
    MIN_COST = (By.XPATH, "//input[@aria-label='Min.']")


    def click_sort_button(self):
        sort_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'a83ed08757') and contains(@class, 'faefc93c6f')]"))
        )
        sort_button.click()

    def click_low_sort(self):
        third_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//ul[contains(@class, 'ad7c39949a')]//button[contains(@class, 'a83ed08757')])[3]"))
        )
        third_button.click()


    def click_heigh_sort(self):
        third_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//ul[contains(@class, 'ad7c39949a')]//button[contains(@class, 'a83ed08757')])[5]"))
        )
        third_button.click()
    def set_min_slider_value(self, value):
        min_slider = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.MIN_COST)
        )

        self.driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
                                   min_slider, value)

    def check_first_card_cost(self):
        first_el = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@data-testid='price-and-discounted-price'])[1]"))
        )
        price_text = first_el.text

        price_match = re.search(r'\d+', price_text.replace("\u00a0", " "))
        if price_match:
            price_value = int(price_match.group())
            if price_value >= 800:
                return True
            else:
                return False
        else:
            return False

