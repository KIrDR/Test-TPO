import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CarRetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.CSS_SELECTOR, "a[data-testid='header-sign-in-button']")
        self.email_input = (By.CSS_SELECTOR, "input[type='email']")
        self.continue_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.sign_in_submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.carRetailLink = "https://www.booking.com/cars/index.html?label=gen173bo-1FCAEoggI46AdIM1gDaCWIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGYAgKoAgO4ApznrrIGwAIB0gIkNWJhNjU1MGYtNzc4Mi00NTU1LWE4ZjctNTFjZGFkNTVlNTEz2AIF4AIB&sid=805285a7efe5a73126f1e429455e96f1&aid=304142&adplat=cross_product_bar"


    def click_sign_in_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.sign_in_button)).click()

    def enter_email(self, email):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.email_input)).send_keys(email)

    def serf_page(self):
        self.driver.execute_script("window.scrollBy(0, window.innerHeight );")


    def click_continue_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.continue_button)).click()

    def enter_password(self, password):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)


    def drop_off_date_click(self):
        dropoff_date_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "searchbox-toolbox-date-picker-dropoff-date"))
        )
        dropoff_date_button.click()

    def click_date_span(self):
        date_span = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'LPCM_3d00354f') and contains(@class, 'LPCM_55351423') and contains(@class, 'LPCM_f34a5d0a') and contains(@class, 'LPCM_688ad363')]"))
        )
        date_span.click()

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[@data-testid='searchbox-toolbox-submit-button' and contains(@class, 'submit-button')]"))
        )
        search_button.click()

    def check_error_message_filled(self):
        try:
            error_message_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "sbc-popover-error-msg-date-time-validation-medium"))
            )
            error_message_text = error_message_element.text

            if error_message_text.strip():
                print("Message: ", error_message_text)
                return True
            else:
                print("Error message is empty.")
                return False
        except Exception as e:
            print("An error occurred:", str(e))
            return False
        time.sleep(1)