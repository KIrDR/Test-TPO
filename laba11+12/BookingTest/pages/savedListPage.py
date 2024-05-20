from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SavedListPage:
    def __init__(self, driver):
        self.driver = driver


    def check_name(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "f829e04eec"))
        )

    def switch_language_to_english(self):
        first_button_conditions = [
            (By.CLASS_NAME, "bui-button--lightхъ"),
            (By.XPATH, "//button[@data-modal-id='language-selection']"),
            (By.XPATH,
             "(//button[@data-et-click=' customGoal:YTTHbXeeVJWcWPaDMWOMHTccTBLWCAWdPZKe:1 customGoal:YTTHbXeeVJWcWPaDMWOMHTcYeIHcUJPUFO:1 '])[2]")
        ]
        language_button = None
        for condition in first_button_conditions:
            try:
                language_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(condition)
                )
                if language_button:
                    language_button.click()
                    break
            except:
                continue

        if not language_button:
            print("Language selection button not found using the provided conditions.")
            return

        second_button_conditions = [
            (By.XPATH, "//button[@data-testid='selection-item']//span[text()='English (US)']"),
            (By.XPATH, "//button[@data-modal-id='language-selection']"),
            (By.XPATH, "//button/span[contains(text(),'English (US)')]")
        ]

        english_option = None
        for condition in second_button_conditions:
            try:
                english_option = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(condition)
                )
                if english_option:
                    english_option.click()
                    break
            except:
                continue

        if not english_option:
            print("English language option not found using the provided conditions.")
            return
