from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base page class with common methods for all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        """Open the given URL"""
        self.driver.get(url)

    def find_element(self, locator):
        """Find element and wait for it to be visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Click on element"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        """Input text into element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from element"""
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False