"""
tests/test_login.py
-------------------
Test suite for SauceDemo login functionality.

Covers:
  - Valid login (standard_user)           [smoke]
  - Locked-out user                        [smoke]
  - Invalid credentials                    [regression]
  - Empty username                         [regression]
  - Empty password                         [regression]
  - Problem user login                     [regression]
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import (
    STANDARD_USER,
    LOCKED_OUT_USER,
    PROBLEM_USER,
    INVALID_USER,
    ErrorMessages,
    PageText,
)


class TestLogin:
    """Test class for SauceDemo login scenarios."""

    # ------------------------------------------------------------------
    # Smoke tests
    # ------------------------------------------------------------------

    @pytest.mark.smoke
    @pytest.mark.login
    def test_valid_login_standard_user(self, login_page: LoginPage):
        """Standard_user can log in successfully and reach the inventory page."""
        login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

        # Should redirect to inventory
        assert login_page.is_logged_in(), (
            f"Expected to be on inventory page, got URL: {login_page.get_current_url()}"
        )

        # Verify product page heading
        inventory = InventoryPage(login_page.page)
        assert inventory.get_page_title() == PageText.PRODUCTS_TITLE

    @pytest.mark.smoke
    @pytest.mark.login
    def test_locked_out_user_shows_error(self, login_page: LoginPage):
        """Locked_out_user should NOT be able to log in and must see an error."""
        login_page.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])

        assert login_page.is_error_displayed(), "Error message should be visible."
        assert login_page.get_error_message() == ErrorMessages.LOCKED_OUT, (
            f"Unexpected error text: {login_page.get_error_message()}"
        )
        assert not login_page.is_logged_in(), "Locked-out user should NOT be on inventory."

    # ------------------------------------------------------------------
    # Regression tests
    # ------------------------------------------------------------------

    @pytest.mark.regression
    @pytest.mark.login
    def test_invalid_credentials_show_error(self, login_page: LoginPage):
        """Invalid username/password combination should show a credentials error."""
        login_page.login(INVALID_USER["username"], INVALID_USER["password"])

        assert login_page.is_error_displayed()
        assert ErrorMessages.INVALID_CREDENTIALS in login_page.get_error_message()
        assert not login_page.is_logged_in()

    @pytest.mark.regression
    @pytest.mark.login
    def test_empty_username_shows_error(self, login_page: LoginPage):
        """Submitting with an empty username should show a validation error."""
        login_page.enter_password(STANDARD_USER["password"])
        login_page.click_login()

        assert login_page.is_error_displayed()
        assert ErrorMessages.USERNAME_REQUIRED in login_page.get_error_message()

    @pytest.mark.regression
    @pytest.mark.login
    def test_empty_password_shows_error(self, login_page: LoginPage):
        """Submitting with an empty password should show a validation error."""
        login_page.enter_username(STANDARD_USER["username"])
        login_page.click_login()

        assert login_page.is_error_displayed()
        assert ErrorMessages.PASSWORD_REQUIRED in login_page.get_error_message()

    @pytest.mark.regression
    @pytest.mark.login
    def test_problem_user_can_login(self, login_page: LoginPage):
        """problem_user should be able to log in (though the site may behave oddly)."""
        login_page.login(PROBLEM_USER["username"], PROBLEM_USER["password"])

        assert login_page.is_logged_in(), (
            "problem_user should successfully authenticate and reach inventory."
        )

    @pytest.mark.regression
    @pytest.mark.login
    def test_error_message_can_be_dismissed(self, login_page: LoginPage):
        """Error banner should disappear when the X close button is clicked."""
        login_page.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])

        assert login_page.is_error_displayed()
        login_page.close_error()
        assert not login_page.is_error_displayed(), (
            "Error message should be gone after closing."
        )

    @pytest.mark.regression
    @pytest.mark.login
    def test_logout_returns_to_login(self, inventory_page: InventoryPage):
        """Logging out from inventory should return to the login page."""
        inventory_page.logout()

        url = inventory_page.get_current_url()
        assert "saucedemo.com" in url
        assert "inventory" not in url, "Should not be on inventory after logout."
