from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage( BasePage ):
    # Selectors
    CONFIRM_DELETE_BUTTON = "VEZI MIN 59"

    # Actions
    def click_delete_by_book_title(self, title):
        self.driver.find_element( By.XPATH, vezi minutul 58 ultimul video)

    def click_confirm_delete_section(self):
        self.wait_for_elem( self.CONFIRM_DELETE_BUTTON )
        self.driver.find_element( By.XPATH, self.CONFIRM_DELETE_BUTTON )


        #validation
        def_validate_book_displayed(self):
        book = self.driver.find_elemens(By.XPATH, '//A[text()= "'+ title + '"]')
        self.assertEqual(1, len(list), 'Book is not present')

        def_validate_book_not_displayed( self ):
        sleep(1)
        self.driver.implicity_wait(1)
        book = self.driver.find_elemens( By.XPATH, '//A[text()= "' + title + '"]' )
        self.assertEqual( 0, len( list ), 'Book is not present' )