from base_page import BasePage
from selenium.webdriver.common.by import By
from urls import BaseUrl


class PasswordResetPage(BasePage):
    Forgot_password_locator = (By.XPATH,
                               "//p[contains(@class,'orangehrm-login-forgot-header')]")
    Username_locator = (By.NAME, 'username')
    Reset_Password_locator = (By.XPATH, "//button[@type='submit']")
    Cancel_password_reset_locator = (By.XPATH, "//button[text()=' Cancel ']")
    Error_message_locator = (By.XPATH, "//span[text()='Required']")
    Password_reset_modal_locator = (By.XPATH,
                                    "//h6[contains(@class,'"
                                    "orangehrm-forgot-password-title')]")

    def click_forgot_password_the_link(self):
        self.open(BaseUrl)
        self.click(self.Forgot_password_locator)

    def reset_password(self, username):
        self.enter(self.Username_locator, username)
        self.click(self.Reset_Password_locator)

    def cancel_password_reset(self):
        self.click(self.Cancel_password_reset_locator)

    def error_message_is_displayed(self):
        return self.is_displayed(self.Error_message_locator)

    def password_reset_modal_is_displayed(self):
        return self.is_displayed(self.Password_reset_modal_locator)
