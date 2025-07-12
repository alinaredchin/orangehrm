from selenium.webdriver.common.by import By
from pages.SidepanelPage import Sidepanel
from urls import BaseUrl


class Header(Sidepanel):

    Header_title_locator = (By.XPATH, "//div[@class='oxd-topbar-header-title']")
    Selected_menu_item_locator = (By.XPATH, "//a[@class='oxd-main-menu-item active']")
    Upgrade_button_locator = (By.XPATH,
                              "//button[contains(@class,"
                              "'orangehrm-upgrade-button')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open_the_link(self):
        self.open(BaseUrl)

    def header_title(self):
        return self.get_text(self.Header_title_locator)
