
Feature: Login capability


  Background:
    Given home: I am a user  on home page
    When home: I click bookstore application card
    When books: I click login button

  @smoke
  Scenario Outline: I login with invalid credentials

    When  login: I login with user "<user>" and "<pswd>"
    Then books: I validate that error message is displayed
  Examples:
    |user|pswd|
    |itfactory.ro|Test123|
    |itfactory.co|Test1223|
    |itfactory.mo|Test12343|


  @regression
  Scenario: I login with valid credentials

    When login: I login with user "itfactory.ro" and "Test123!"
    Then books: I should land on books page






