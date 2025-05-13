from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Inventory page object model"""

    # Locators
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[class*='btn_inventory']")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def is_inventory_page_loaded(self):
        """Check if inventory page is loaded"""
        return self.is_element_visible(self.INVENTORY_CONTAINER)

    def get_product_names(self):
        """Get list of product names"""
        self.wait.until(lambda d: len(d.find_elements(*self.PRODUCT_NAMES)) > 0)
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def add_product_to_cart(self, index=0):
        """Add product to cart by index"""
        self.wait.until(lambda d: len(d.find_elements(*self.ADD_TO_CART_BUTTONS)) > 0)
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)

        if 0 <= index < len(buttons):
            # Get the product name before adding to cart
            product_names = self.get_product_names()
            product_name = product_names[index] if index < len(product_names) else None

            # Click the add to cart button
            buttons[index].click()

            return product_name
        else:
            raise IndexError(f"Product index {index} out of range")

    def go_to_cart(self):
        """Go to shopping cart"""
        self.click_element(self.CART_BUTTON)