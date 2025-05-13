from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Cart page object model"""

    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def is_cart_page_loaded(self):
        """Check if cart page is loaded"""
        return self.is_element_visible(self.CHECKOUT_BUTTON)

    def get_cart_items(self):
        """Get list of cart item names"""
        if not self.driver.find_elements(*self.CART_ITEMS):
            return []

        self.wait.until(lambda d: len(d.find_elements(*self.CART_ITEM_NAMES)) > 0)
        elements = self.driver.find_elements(*self.CART_ITEM_NAMES)
        return [element.text for element in elements]

    def is_product_in_cart(self, product_name):
        """Check if product is in cart"""
        cart_items = self.get_cart_items()
        return product_name in cart_items