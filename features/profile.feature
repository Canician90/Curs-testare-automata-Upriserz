Feature: Profile capability


  @regression
  Scenario Outline: I add/remove books to my collection
    Given home: I am a user  on home page
    When home: I click bookstore application card
    When books: I click login button
    When login: I login with user "itfactory.ro" and "Test123!"
    When books: I add  to collection the book with title "<book1>"
    When books: I add  to collection the book with title "<book2>"
    When menu: I click profile_section
    Then profile: Book with title "<book1>" is present in collection
    Then profile: Book with title "<book2>" is present in collection
    When menu: I remove the book with tittle "Git Pocket Guide" from collection
    Then profile: Book with title "<book1>" is not present in collection
    Then profile: Book with title "<book2>" is present in collection
    When profile: I remove the book with tittle "<book2>" from collection
    Then profile: Book with title "<book2>" is not present in collection


    Examples:
    |book1             |book2|
    |Git Pocket Guide  |Speaking JavaScript|