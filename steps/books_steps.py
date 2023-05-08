from pages.home_page import  HomePage
from behave import *


books_page = BooksPage()


@when ('books: I click login button')
def step_impl(context):
    home_page.click_login_button()

    @Then('books: I should land on books page')
    def step_impl(context):
    books_page.validate_current_url()


    #pages -> steps