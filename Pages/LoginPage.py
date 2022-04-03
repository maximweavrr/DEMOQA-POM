from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class LoginPage(BasePage):
    
    # LOCATORS IN LOGIN PAGE
    email_locator = (By.ID, "userName")
    password_locator = (By.ID, "password")
    login_button = (By.ID, "login")
    new_user_button = (By.ID, "newUser")


    # METHOD IN SPECIFIC PAGE ACTIONS
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self,title):
        return self.get_title(title)
    
    def is_NewUser_Button(self):
        return self.is_visible(self.new_user_button)

    def enter_Email(self, USER_NAME):
        self.do_sendKeys(self.email_locator, USER_NAME)

    def enter_Pass(self, PASSWORD):
        self.do_sendKeys(self.password_locator, PASSWORD)

    def do_login(self):
        self.do_click(self.login_button)