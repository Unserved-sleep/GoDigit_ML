"""
pages/login_page.py
-------------------
Page Object for the SauceDemo Login page.
URL: https://www.saucedemo.com/
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Encapsulates all interactions with the SauceDemo login page."""

    # ------------------------------------------------------------------
    # Selectors
    # ------------------------------------------------------------------
    USERNAME_INPUT: str = "#user-name"
    PASSWORD_INPUT: str = "#password"
    LOGIN_BUTTON: str = "#login-button"
    ERROR_MESSAGE: str = "[data-test='error']"
    ERROR_CLOSE_BUTTON: str = ".error-button"
    LOGIN_LOGO: str = ".login_logo"
    LOGIN_CREDENTIALS: str = "#login_credentials"

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def open(self) -> "LoginPage":
        """Navigate to the login page."""
        self.navigate("https://www.saucedemo.com/")
        return self

    def enter_username(self, username: str) -> "LoginPage":
        self.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """
        Perform a full login sequence:
        enter username, password, and click login.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def close_error(self) -> None:
        """Dismiss the error message banner."""
        if self.is_visible(self.ERROR_CLOSE_BUTTON):
            self.click(self.ERROR_CLOSE_BUTTON)

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_error_message(self) -> str:
        """Return the text of the error message container."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        """
        Returns True if the browser has navigated away from the login page
        (i.e., is now on inventory).
        """
        return "inventory" in self.get_current_url()

    def get_logo_text(self) -> str:
        return self.get_text(self.LOGIN_LOGO)

    def get_username_field_value(self) -> str:
        return self.page.locator(self.USERNAME_INPUT).input_value()

    def get_password_field_value(self) -> str:
        return self.page.locator(self.PASSWORD_INPUT).input_value()
