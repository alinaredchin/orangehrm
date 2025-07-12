from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from urls import BaseUrl


class Sidepanel(LoginPage):
    Sidepanel_locator = (By.XPATH, "//nav[@class='oxd-navbar-nav']")
    Sidepanel_button_locator = (
        By.XPATH, "//button[contains(@class,'oxd-main-menu-button')]"
    )
    Sidepanel_closed_locator = (
        By.XPATH, "//i[contains(@class,'oxd-icon bi-chevron-right')]"
    )
    Search_field_locator = (By.XPATH, "//input[contains(@class,'oxd-input')]")
    Sidepanel_menu = (By.XPATH, "//ul[@class='oxd-main-menu']")
    Sidepanel_items = (
        By.XPATH, "//a[contains(@class,'toggle')][contains(@class,'menu-item')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open_the_link(self):
        self.open(BaseUrl)

    def hide_the_sidepanel(self):
        self.click(self.Sidepanel_button_locator)

    def is_sidepanel_collapsed(self):
        return self.is_displayed(self.Sidepanel_closed_locator)

    def is_search_field_clickable(self):
        return self.is_clickable(5, self.Search_field_locator)

    def search(self, text):
        self.is_clickable(5, self.Search_field_locator)
        self.enter(self.Search_field_locator, text)

    def get_list_of_items(self):
        items = self.find_all(self.Sidepanel_items)
        print(items)
        return items
