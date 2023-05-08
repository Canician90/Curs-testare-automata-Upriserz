from selenium.webdriver.common.by import By
from pages.base_page import BasePage




class LeftMenu(BasePage):

        #Selectors
        LOGIN_BUTTON ='//span[@text()="Profile"]'

        #Actions
        def click_profile_section(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH.self.LOGIN_BUTTON).click()
