from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from urls import BaseUrl


class Sidepanel(LoginPage):
    Sidepanel_locator = (By.XPATH, "//nav[@class='oxd-navbar-nav']")
    Sidepanel_button_locator = (
        By.XPATH, "//button[contains(@class,'oxd-main-menu-button')]"
    )
    Sidepanel_closed_locator = (By.XPATH, "//aside[@class='oxd-sidepanel']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_the_link(self):
        self.open(BaseUrl)

    def is_element_present(self):
        return self.is_displayed(self.Sidepanel_locator)

    def hide_the_sidepanel(self):
        self.click(self.Sidepanel_button_locator)

    def is_sidepanel_collapsed(self):
        return self.is_displayed(self.Sidepanel_closed_locator)
