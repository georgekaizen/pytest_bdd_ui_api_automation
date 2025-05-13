from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object model"""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        """Open the login page"""
        self.open_url(self.url)
        return self

    def login(self, username, password):
        """Login with provided credentials"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        return self

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)