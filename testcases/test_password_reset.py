from pages.PasswordResetPage import PasswordResetPage


class TestPasswordReset:

    def test_successful_password_reset(self, driver):
        password_reset_page = PasswordResetPage(driver)
        password_reset_page.click_forgot_password_the_link()
        password_reset_page.reset_password("Admin")
        assert password_reset_page.password_reset_modal_is_displayed()
