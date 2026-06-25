from playwright.sync_api import Page

class CartPage:
    def __init__(self, page):
        self.page = page

    def cart_item_count(self):
        return self.page.locator(".inventory_item_name").count()

    def remove_from_cart(self, item_name):
        self.page.locator(".cart_item"
                          ).filter(has_text= item_name
                                   ).locator("button").click()
    def cart_items(self):
        return self.page.locator(".shopping_cart_badge").text_content()

    def checkout(self):
        self.page.locator("[name='checkout']").click()