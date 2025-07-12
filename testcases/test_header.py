import urls
from pages.Header import Header


class TestHeader:

    def test_header_title(self, driver):
        header = Header(driver)
        header.open_the_link()
        header.login("Admin", "admin123")
        header_title_text = header.header_title()
        selected_menu_item = header.Selected_menu_item_locator
        selected_menu_item_text = header.get_text(selected_menu_item)
        assert header_title_text == selected_menu_item_text

    def test_redirect_to_upgrade_page(self, driver):
        header = Header(driver)
        header.open_the_link()
        header.login("Admin", "admin123")
        header.click(header.Upgrade_button_locator)
        header.switch_to_a_new_tab()
        assert header.get_current_url() == urls.Upgrade_page_url
