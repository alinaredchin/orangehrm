from pages.SidepanelPage import Sidepanel


class TestSidepanel:

    def test_sidepanel_is_present(self, driver):
        sidepanel = Sidepanel(driver)
        sidepanel.open_the_link()
        sidepanel.login("Admin", "admin123")
        assert sidepanel.is_displayed(sidepanel.Sidepanel_locator)

    def test_close_sidepanel(self, driver):
        sidepanel = Sidepanel(driver)
        sidepanel.open_the_link()
        sidepanel.login("Admin", "admin123")
        sidepanel.hide_the_sidepanel()
        assert sidepanel.is_sidepanel_collapsed()

    def test_search_field(self, driver):
        sidepanel = Sidepanel(driver)
        sidepanel.open_the_link()
        sidepanel.login("Admin", "admin123")
        sidepanel.search('Admin')
        suggestions = sidepanel.wait_until_all_elements_are_visible(
            5, sidepanel.Sidepanel_menu)
        for suggestion in suggestions:
            text = suggestion.text
            assert 'Admin' in text, f"Suggestion {text} doesn't contain 'Admin'"
