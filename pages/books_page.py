from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class BooksPage(BasePage):

        #Selectors
        LOGIN_BUTTON = '//button[@id="login"]'


        #actions


            def click_login_button (self):
            self.wait_for_elem(self.LOGIN_BUTTON)
            self.driver.find_element(By.XPATH. self.LOGIN_BUTTON).click()


        #validations