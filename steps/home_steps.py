from pages.home_page import  HomePage
from behave import *


#given -seteaza situatia intiala
#when - actiunile intermediare
#then - verificarea finala


#  Behavior Driven Development Framework  - uniformizeaza comunicarea tuturor membrilor

'''
Given I am a user on home page
When I click bookstore application card
When I click login button
When I login with valid credentials
Then I should land on books page
'''




home_page = HomePage()

@given ('home: I am a user  on home page')
def step_impl(context):
    home_page.navigate_to_home_page()


@when ('home: I click bookstore application card')
def step_impl(context):
    home_page.click_book_store_application_card()