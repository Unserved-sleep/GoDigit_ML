"""
conftest.py
-----------
Root-level pytest fixtures for the SauceDemo Playwright framework.

Fixtures provided:
  - browser_context  : Playwright BrowserContext with tracing enabled
  - page             : Fresh page per test (from browser_context)
  - logged_in_page   : Page already authenticated as standard_user
  - login_page       : LoginPage instance on a fresh page
  - inventory_page   : InventoryPage instance on a logged-in page
  - cart_page        : CartPage instance on a logged-in page
  - checkout_page    : CheckoutPage instance on a logged-in page
  - take_screenshot  : Callable fixture to capture screenshots on demand

Auto-use fixture:
  - auto_artifact    : Captures screenshot + stops trace on test FAILURE
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from datetime import datetime

import pytest
from playwright.sync_api import Page, BrowserContext, Browser, Playwright

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import STANDARD_USER

# ---------------------------------------------------------------------------
# Directory setup
# ---------------------------------------------------------------------------
ROOT_DIR = Path(__file__).parent
SCREENSHOTS_DIR = ROOT_DIR / "screenshots"
TRACES_DIR = ROOT_DIR / "traces"
REPORTS_DIR = ROOT_DIR / "reports"

for _dir in (SCREENSHOTS_DIR, TRACES_DIR, REPORTS_DIR):
    _dir.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _safe_name(test_name: str) -> str:
    """Convert a test nodeid into a filesystem-safe string."""
    return re.sub(r"[^\w\-]", "_", test_name)[:120]


# ---------------------------------------------------------------------------
# Browser context with tracing
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def browser_context(browser: Browser, request) -> BrowserContext:
    """
    Create a new BrowserContext for each test with:
      - viewport: 1280×720
      - Playwright tracing started (screenshots + snapshots)
    """
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir=None,  # disable video by default; enable with --video flag
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context

    # ---------- teardown ----------
    test_name = _safe_name(request.node.nodeid)
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        trace_path = TRACES_DIR / f"{test_name}.zip"
        context.tracing.stop(path=str(trace_path))
    else:
        context.tracing.stop()

    context.close()


# ---------------------------------------------------------------------------
# Per-test page
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def page(browser_context: BrowserContext) -> Page:
    """Return a fresh Page from the browser_context."""
    page = browser_context.new_page()
    yield page
    page.close()


# ---------------------------------------------------------------------------
# Auto-capture screenshot on failure
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function", autouse=True)
def auto_artifact(page: Page, request) -> None:
    """
    Auto-use fixture that captures a full-page screenshot when a test FAILS.
    The screenshot is named after the test and saved to screenshots/.
    """
    yield

    # Only capture on actual test-call failures (not setup/teardown)
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        test_name = _safe_name(request.node.nodeid)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = SCREENSHOTS_DIR / f"FAIL_{test_name}_{timestamp}.png"
        try:
            page.screenshot(path=str(path), full_page=True)
            print(f"\n📸 Failure screenshot saved: {path}")
        except Exception as e:
            print(f"\n⚠️  Could not capture screenshot: {e}")


# ---------------------------------------------------------------------------
# pytest hook: attach rep_call to request.node
# ---------------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Store the test result on the node so fixtures can access it during teardown.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ---------------------------------------------------------------------------
# Logged-in page
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def logged_in_page(page: Page) -> Page:
    """
    Navigate to login, authenticate as standard_user, and return the page
    already on the inventory screen.
    """
    login = LoginPage(page)
    login.open()
    login.login(STANDARD_USER["username"], STANDARD_USER["password"])
    # Ensure we've landed on inventory
    page.wait_for_url("**/inventory.html")
    return page


# ---------------------------------------------------------------------------
# Page object fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    """Return a LoginPage instance with the login URL already open."""
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture(scope="function")
def inventory_page(logged_in_page: Page) -> InventoryPage:
    """Return an InventoryPage instance on a logged-in page."""
    return InventoryPage(logged_in_page)


@pytest.fixture(scope="function")
def cart_page(logged_in_page: Page) -> CartPage:
    """Return a CartPage instance on a logged-in page."""
    cp = CartPage(logged_in_page)
    cp.open()
    return cp


@pytest.fixture(scope="function")
def checkout_page(logged_in_page: Page) -> CheckoutPage:
    """Return a CheckoutPage instance (used after items are in cart)."""
    return CheckoutPage(logged_in_page)


# ---------------------------------------------------------------------------
# On-demand screenshot callable
# ---------------------------------------------------------------------------

@pytest.fixture(scope="function")
def take_screenshot(page: Page):
    """
    Returns a callable: take_screenshot(name: str) -> str
    Saves a full-page screenshot to screenshots/<name>.png and returns the path.
    """
    def _capture(name: str) -> str:
        path = SCREENSHOTS_DIR / f"{name}.png"
        page.screenshot(path=str(path), full_page=True)
        return str(path)

    return _capture


# ---------------------------------------------------------------------------
# pytest-html: attach screenshots to the HTML report
# ---------------------------------------------------------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    yield


def pytest_configure(config):
    """Ensure reports directory exists before pytest-html writes to it."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
