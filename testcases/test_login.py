from pages.loginpage import LoginPage


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

    def test_error_message(self, driver):
        login_page = LoginPage(driver)
        login_page.login("Invalid login", "invalidpassword123")
        error_message = login_page.error_text_message()

        assert error_message == "Invalid credentials", "Incorrect error message"
        
        
