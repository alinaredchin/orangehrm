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

    def test_nav_items_names_are_hidden_when_menu_is_collapsed(self, driver):
        sidepanel = Sidepanel(driver)
        sidepanel.open_the_link()
        sidepanel.login("Admin", "admin123")
        sidepanel.hide_the_sidepanel()
        assert sidepanel.nav_items_names_are_hidden()

    def test_search_field(self, driver):
        sidepanel = Sidepanel(driver)
        sidepanel.open_the_link()
        sidepanel.login("Admin", "admin123")
        sidepanel.search('Admin')
        suggestions = sidepanel.get_list_of_items()
        for suggestion in suggestions:
            menu_item = suggestion.text
            assert 'Admin' in menu_item, (
                f"Suggestion {menu_item} doesn't contain 'Admin'"
            )
