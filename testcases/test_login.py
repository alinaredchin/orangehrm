import pytest
from pages.loginpage import LoginPage
from conftest import driver


class TestLogin:

    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")
        expected_url = login_page.expected_url
        current_url = login_page.get_current_url()

        assert current_url == expected_url

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("Invalid login", "invalidpassword123")

        assert login_page.is_error_message_displayed()


