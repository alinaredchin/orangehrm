import pytest
from conftest import browser
from pages.loginpage import LoginPage


@pytest.mark.usefixtures("browser")
class TestLogin:

    def test_valid_login(self, browser):
        login_page = LoginPage(browser)
        login_page.login("Admin", "admin123")
        expected_url = login_page.expected_url
        current_url = login_page.get_current_url()

        assert current_url == expected_url

    def test_invalid_login(self, browser):
        login_page = LoginPage(browser)
        login_page.login("Invalid login", "invalidpassword123")

        error_message = login_page.is_error_message_displayed()

        assert error_message



