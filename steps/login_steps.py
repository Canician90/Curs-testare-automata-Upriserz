from pages.login_page import  LoginPage
from behave import *


login_page = LoginPage()


@when ('login: I login with valid credentials)
def step_impl(context):
    login_page.fill_pass_input('itfactory.ro')
    login_page.fill_pass_input('Test123!')
    login_page.click_login_button()
