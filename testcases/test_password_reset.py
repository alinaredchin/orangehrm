import urls
from pages.PasswordResetPage import PasswordResetPage


class TestPasswordReset:

    def test_successful_password_reset(self, driver):
        password_reset_page = PasswordResetPage(driver)
        password_reset_page.click_forgot_password_the_link()
        password_reset_page.reset_password("Admin")
        assert password_reset_page.password_reset_modal_is_displayed()

    def test_unsuccessful_password_reset(self, driver):
        password_reset_page = PasswordResetPage(driver)
        password_reset_page.click_forgot_password_the_link()
        password_reset_page.reset_password("")
        assert password_reset_page.error_message_is_displayed

    def test_cancel_password_reset(self, driver):
        password_reset_page = PasswordResetPage(driver)
        password_reset_page.click_forgot_password_the_link()
        password_reset_page.cancel_password_reset()
        current_page = password_reset_page.current_url
        assert current_page == urls.BaseUrl
