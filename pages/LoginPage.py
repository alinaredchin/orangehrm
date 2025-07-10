import urls
from base_page import BasePage
from selenium.webdriver.common.by import By
from urls import BaseUrl


class LoginPage(BasePage):
    username_locator = (By.NAME, 'username')
    password_locator = (By.NAME, 'password')
    login_locator = (By.XPATH, '//button')
    error_message_locator = (By.CSS_SELECTOR, '.oxd-alert.oxd-alert--error')
    forgot_your_password_locator = (By.XPATH, '//p[text()="Forgot your password? "]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_the_link(self):
        self.open(BaseUrl)

    def login(self, username, password):
        self.enter(self.username_locator, username)
        self.enter(self.password_locator, password)
        self.click(self.login_locator)

    @property
    def expected_url(self) -> str:
        return urls.Logged_in_successfully_url

    def get_current_url(self):
        return super().current_url

    def is_error_message_displayed(self) -> bool:
        return self.is_displayed(self.error_message_locator)

    def error_text_message(self):
        return self.get_text(self.error_message_locator)

    def click_forgot_you_password(self):
        self.click(self.forgot_your_password_locator)

