import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Import the feature file scenarios
scenarios('../api_countries.feature')

# Global variables to store state between steps
CURRENCY_CODE = None
API_RESPONSE = None


@given(parsers.parse('I have a valid currency code "{currency_code}"'))
def set_valid_currency_code(currency_code):
    global CURRENCY_CODE
    CURRENCY_CODE = currency_code


@given(parsers.parse('I have an invalid currency code "{currency_code}"'))
def set_invalid_currency_code(currency_code):
    global CURRENCY_CODE
    CURRENCY_CODE = currency_code


@when('I make a GET request to the countries API')
def make_api_request():
    global CURRENCY_CODE, API_RESPONSE
    url = f"https://restcountries.com/v3.1/currency/{CURRENCY_CODE}"
    API_RESPONSE = requests.get(url)


@then(parsers.parse('I should receive a successful response with status code {status_code:d}'))
def verify_success_status_code(status_code):
    global API_RESPONSE
    assert API_RESPONSE.status_code == status_code, f"Expected status code {status_code}, got {API_RESPONSE.status_code}"


@then(parsers.parse('I should receive an error response with status code {status_code:d}'))
def verify_error_status_code(status_code):
    global API_RESPONSE
    assert API_RESPONSE.status_code == status_code, f"Expected status code {status_code}, got {API_RESPONSE.status_code}"


@then('I should see at least one country in the response')
def verify_countries_present():
    global API_RESPONSE
    countries = API_RESPONSE.json()
    assert len(countries) > 0, "No countries found in the response"


@then('I should be able to extract a country name')
def extract_country_name():
    global API_RESPONSE
    countries = API_RESPONSE.json()
    # Extract the first country's name
    country_name = countries[0]["name"]["common"]
    assert country_name, f"Country name is empty or not found"
    print(f"Found country: {country_name}")


@then('I should see an appropriate error message')
def verify_error_message():
    global API_RESPONSE
    response_data = API_RESPONSE.json()
    assert "message" in response_data, "Error response does not contain 'message' field"
    assert "Not Found" in response_data["message"], f"Unexpected error message: {response_data['message']}"