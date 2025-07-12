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
