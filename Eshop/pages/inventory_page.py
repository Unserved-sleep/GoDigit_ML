from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.item_list = page.locator(".inventory_item_name")

    def item_count(self):
        return self.item_list.count()

    def item_name(self):
        return self.item_list.all_text_contents()

    def item_is_in_stock(self, item_list):
        return self.page.locator(f'.inventory_item_name:test-is("{item_list}")').is_visible()

    def add_to_cart(self, item_name):
        self.page.locator(".inventory_item"
                          ).filter(has_text=item_name
                                   ).locator("button").click()

    def remove_from_cart(self, item_name):
        self.page.locator(".inventory_item"
                          ).filter(has_text=item_name
                                   ).locator("button").click()

    def cart_items(self):
        return self.page.locator(".shopping_cart_badge").text_content()

    def open_cart_page(self):
        self.page.locator(".shopping_cart_link").click()
