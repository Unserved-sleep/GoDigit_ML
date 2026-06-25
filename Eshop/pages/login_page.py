from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def open_login_page(self):
        self.page.goto("https://www.saucedemo.com/")

    def get_username(self, username):
        self.username.fill(username)

    def get_password(self, password):
        self.password.fill(password)

    def login(self, username, password):
        self.get_username(username)
        self.get_password(password)
        self.login_button.click()