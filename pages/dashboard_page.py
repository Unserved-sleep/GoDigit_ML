from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Dashboard")
        self.welcome_message = page.get_by_text("Welcome, admin!")
        self.logout_button = page.get_by_role("button", name="Logout")

    def logout(self):
        """Perform logout action by clicking the logout button."""
        self.logout_button.click()
