from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")

    def fill_details(self):
        # Wait and fill
        first = self.wait.until(EC.visibility_of_element_located(self.first_name))
        first.clear()
        first.send_keys("Test")

        last = self.driver.find_element(*self.last_name)
        last.clear()
        last.send_keys("User")

        pin = self.driver.find_element(*self.postal_code)
        pin.clear()
        pin.send_keys("12345")

        # 🔥 DEBUG PRINT (IMPORTANT)
        print("First Name:", first.get_attribute("value"))
        print("Last Name:", last.get_attribute("value"))
        print("Postal Code:", pin.get_attribute("value"))

    def continue_checkout(self):
        self.driver.find_element(*self.continue_btn).click()

        # 🔥 DEBUG: URL check
        print("After continue URL:", self.driver.current_url)

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_btn)).click()