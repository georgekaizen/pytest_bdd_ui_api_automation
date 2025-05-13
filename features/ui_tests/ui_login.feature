Feature: SauceDemo Login and Cart Functionality
  As a user of SauceDemo
  I want to be able to login and use the shopping cart
  So that I can shop for products effectively

  Scenario: Happy Path - Login, add product to cart, and verify
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page
    When I add a product to the cart
    And I go to the cart page
    Then I should see the product in the cart

  Scenario: Unhappy Path - Login with incorrect credentials
    Given I am on the SauceDemo login page
    When I login with username "invalid_user" and password "wrong_password"
    Then I should see an error message
    And The error message should contain "Username and password do not match"