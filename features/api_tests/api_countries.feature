Feature: REST Countries API Currency Testing
  As a user of the REST Countries API
  I want to retrieve country data based on currency
  So that I can get information about countries using specific currencies

  Scenario: Happy Path - Get countries by valid currency code
    Given I have a valid currency code "KES"
    When I make a GET request to the countries API
    Then I should receive a successful response with status code 200
    And I should see at least one country in the response
    And I should be able to extract a country name

  Scenario: Unhappy Path - Get error for non-existent currency code
    Given I have an invalid currency code "XYZ"
    When I make a GET request to the countries API
    Then I should receive an error response with status code 404
    And I should see an appropriate error message