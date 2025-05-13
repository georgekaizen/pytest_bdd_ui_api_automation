import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Import the feature file scenarios
scenarios('../ui_login.feature')

# Global variables to store state between steps
PRODUCT_NAME = None


@given("I am on the SauceDemo login page")
def navigate_to_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open()


@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login_with_credentials(browser, username, password):
    login_page = LoginPage(browser)
    login_page.login(username, password)


@then("I should be redirected to the inventory page")
def verify_inventory_page(browser):
    inventory_page = InventoryPage(browser)
    assert inventory_page.is_inventory_page_loaded(), "Inventory page did not load"


@when("I add a product to the cart")
def add_product_to_cart(browser):
    global PRODUCT_NAME
    inventory_page = InventoryPage(browser)
    PRODUCT_NAME = inventory_page.add_product_to_cart(0)
    assert PRODUCT_NAME is not None, "Failed to get product name"


@when("I go to the cart page")
def go_to_cart_page(browser):
    inventory_page = InventoryPage(browser)
    inventory_page.go_to_cart()


@then("I should see the product in the cart")
def verify_product_in_cart(browser):
    global PRODUCT_NAME
    cart_page = CartPage(browser)
    assert cart_page.is_cart_page_loaded(), "Cart page did not load"
    assert cart_page.is_product_in_cart(PRODUCT_NAME), f"Product '{PRODUCT_NAME}' not found in cart"


@then("I should see an error message")
def verify_error_message_displayed(browser):
    login_page = LoginPage(browser)
    assert login_page.is_element_visible(login_page.ERROR_MESSAGE), "Error message not displayed"


@then(parsers.parse('The error message should contain "{text}"'))
def verify_error_message_content(browser, text):
    login_page = LoginPage(browser)
    error_message = login_page.get_error_message()
    assert text in error_message, f"Error message '{error_message}' does not contain '{text}'"