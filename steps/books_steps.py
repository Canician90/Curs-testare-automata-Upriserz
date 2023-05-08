from pages.home_page import  HomePage
from behave import *


books_page = BooksPage()


@when ('books: I click login button')
def step_impl(context):
    home_page.click_login_button()

    @when('books: I search after "{query}"')
    def step_impl(context, query):
        home_page.fill_search_input(query)

        @when('books: I clear search input')
        def step_impl(context):
            home_page.clear_search_input()

    @Then('books: I should land on books page')
    def step_impl(context):
    books_page.validate_current_url()

    @Then('books: I validate that 8 books are displayed')
    def step_impl(context):
        books_page.validate_books_count(8)

        @Then('books: I validate that only"{title}" book is displayed')
        def step_impl(context):
            books_page.validate_books_count(0)
            books_page.validate_book_title(title)


    #pages -> steps