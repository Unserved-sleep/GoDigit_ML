from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(page):
    """Verify that a user can log in with valid credentials and log out successfully."""
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # 1. Navigate to the login page
    login_page.navigate()

    # 2. Perform login with valid credentials
    login_page.login("admin", "admin123")

    # 3. Assert dashboard elements are visible and active
    assert dashboard_page.heading.is_visible(), "Dashboard heading is not visible"
    assert dashboard_page.welcome_message.is_visible(), "Welcome message is not visible"
    assert dashboard_page.logout_button.is_enabled(), "Logout button is not enabled"

    # 4. Perform logout
    dashboard_page.logout()

    # 5. Assert redirection back to login page
    assert login_page.login_button.is_visible(), "Login button is not visible after logout"


def test_invalid_login(page):
    """Verify that appropriate error message is displayed on invalid login attempt."""
    login_page = LoginPage(page)

    # 1. Navigate to the login page
    login_page.navigate()

    # 2. Attempt login with invalid credentials
    login_page.login("wrong_user", "wrong_pass")

    # 3. Assert error message is visible and login button remains visible
    assert login_page.error_message.is_visible(), "Error message was not displayed for invalid credentials"
    assert login_page.login_button.is_visible(), "Login button is not visible after failed login"
