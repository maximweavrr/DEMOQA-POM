import pytest
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage

class TestLogin(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_NewUser_Button()
        assert flag