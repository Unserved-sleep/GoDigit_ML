from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_information(self):
        self.page.get_by_placeholder("First Name").fill("abc")
        self.page.get_by_placeholder("Last Name").fill("abc")
        self.page.get_by_placeholder("Zip/Postal Code").fill("123456")
        self.page.locator("[type='submit']").click()

    def place_order(self):
        self.page.locator("[name='finish']").click()

    def validation(self):
        return self.page.locator(".complete-header").text_content()