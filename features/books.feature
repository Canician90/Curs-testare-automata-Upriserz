Feature: Books capability


  Background:
    Given home: I am a user  on home page
    When home: I click bookstore application card
    When books: I click login button
    When login: I login with user "itfactory.ro" and "Test123!"

  @books
    Scenario: I validate the stock count
    Then books: I validate that 8 books are displayed

  @books


  Scenario Outline:I validate the search is working
    When I search after "<query>"


    Then books: I validate that only "Git Pocket Guide" books are displayed

    Examples:
    |query|
    |Git  |
    |Richard|


     @test
    Scenario: I validate that clear search is working
       When I search after "test"
       When  books: I clear  search input
    Then books: I validate that 8 books are displayed


