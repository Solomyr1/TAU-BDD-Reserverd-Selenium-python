Feature: register on reserved website

Scenario: test register successfully
    Given open the register page
    When the user type email "test@yahoo.com"
    And the user type name "ion"
    And the user type lastname"ion"
    And the user type password "start123"
    And the user click Create Account button
    Then Check the user account has been created