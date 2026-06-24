from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_text("Invalid username or password")

    def navigate(self):
        """Navigate to the mock login page."""
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        """Fill in credentials and submit the login form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
