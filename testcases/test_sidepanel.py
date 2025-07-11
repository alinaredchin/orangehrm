from pages.SidepanelPage import Sidepanel


class TestSidepanel:

    def test_sidepanel_is_present(self, driver):
        sidepanel = Sidepanel(driver)
        sidepanel.open_the_link()
        sidepanel.login("Admin", "admin123")
        assert sidepanel.is_element_present()

    def test_close_sidepanel(self, driver):
        sidepanel = Sidepanel(driver)
        sidepanel.open_the_link()
        sidepanel.login("Admin", "admin123")
        sidepanel.hide_the_sidepanel()
        assert sidepanel.is_sidepanel_collapsed()
