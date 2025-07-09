from base_page import BasePage
from selenium.webdriver.common.by import By

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


class LoginPage(BasePage):
    username_locator = (By.NAME, 'username')
    password_locator = (By.NAME, 'password')
    login_locator = (By.XPATH, '//button')
    error_message_locator = (By.CLASS_NAME, 'oxd-alert oxd-alert--error')

    Expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.open(BaseUrl)
        self.enter(self.username_locator, username)  # we use 'self' before login_locator because its in the same class
        self.enter(self.password_locator, password)
        self.click(self.login_locator)

    @property
    def expected_url(self) -> str:
        return self.Expected_url

    def get_current_url(self):
        return super().current_url

    def is_error_message_displayed(self):
        return self.is_displayed(self.error_message_locator)
