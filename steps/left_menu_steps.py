from pages.left_menu import LeftMenu
from behave import *


Left_menu = LeftMenu()


@when('menu: I click profile_section')
def step_impl(context):
    left_menu.click_profile_section()



