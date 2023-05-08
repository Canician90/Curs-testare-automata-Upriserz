from pages.home_page import  HomePage
from behave import *
from time import sleep


books_page = BooksPage()


@when ('books: I click login button')
def step_impl(context):
    sleep(5)
    home_page.click_login_button()

    @when('books: I search after "{query}"')
    def step_impl(context, query):
        home_page.fill_search_input(query)

        @when( 'books: I add  to collection the book with title "{title}"' )
        def step_impl(context, title):
            books_page.click_book_by_title(title)
            books_page.click_add_to_your_collection_button()
            books_page.browser_back()



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