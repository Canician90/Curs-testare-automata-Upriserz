from pages.login_page import  LoginPage
from behave import *


login_page = LoginPage()


@when ('login: I login with user "{user} and "{paswd}"')
def step_impl(context, user, pswd):
    login_page.fill_pass_input('itfactory.ro')
    login_page.fill_pass_input('Test123!')
    login_page.click_login_button()
    login_page.back()



        @then('login: I validate that error message is displayed')
        def step_impl(context):
            login_page.validate_invalid_credentials_error()
