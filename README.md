# SauceDemo Test Project

This project contains automated tests for:
1. UI testing of SauceDemo website
2. API testing of RestCountries currency endpoint

## Setup

1. Clone this repository
2. Install dependencies:
```
pip install -r requirements.txt
```

## Running Tests

### Run all tests
```
pytest
```

### Run only UI tests
```
pytest features/ui_tests/steps/ui_steps.py
```

### Run only API tests
```
pytest features/api_tests/steps/api_steps.py
```

## Project Structure

- `features/` - Contains BDD feature files and step definitions
  - `ui_tests/` - UI test features and steps
  - `api_tests/` - API test features and steps
- `pages/` - Page Object Model implementation
- `conftest.py` - Pytest fixtures and configuration

## Test Scenarios

### UI Tests
1. Happy Path - Login, add product to cart, verify cart
2. Unhappy Path - Login with incorrect credentials, verify error message

### API Tests
1. Happy Path - Get countries by valid currency code
2. Unhappy Path - Get error for non-existent currency code