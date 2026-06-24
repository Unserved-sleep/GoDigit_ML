"""
pages/base_page.py
------------------
BasePage provides shared utilities used by all page objects:
  - Navigation
  - Element waiting
  - Screenshot capture
  - Text extraction
  - URL/title assertions
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError


SCREENSHOTS_DIR = Path(__file__).parent.parent / "screenshots"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


class BasePage:
    """Base class for all Page Objects."""

    # Default timeout (ms) for element interactions
    DEFAULT_TIMEOUT: int = 10_000

    def __init__(self, page: Page) -> None:
        self.page = page

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    def navigate(self, url: str) -> None:
        """Navigate to an absolute URL or relative path."""
        self.page.goto(url, wait_until="domcontentloaded")

    def get_current_url(self) -> str:
        return self.page.url

    def get_title(self) -> str:
        return self.page.title()

    def go_back(self) -> None:
        self.page.go_back(wait_until="domcontentloaded")

    # ------------------------------------------------------------------
    # Element helpers
    # ------------------------------------------------------------------

    def wait_for_element(
        self, selector: str, timeout: int = DEFAULT_TIMEOUT
    ) -> Locator:
        """Wait for an element to be visible and return its Locator."""
        locator = self.page.locator(selector)
        locator.wait_for(state="visible", timeout=timeout)
        return locator

    def get_text(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> str:
        """Return the inner text of the first matching element."""
        return self.wait_for_element(selector, timeout).inner_text()

    def click(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        self.wait_for_element(selector, timeout).click()

    def fill(self, selector: str, value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.wait_for_element(selector, timeout)
        element.clear()
        element.fill(value)

    def is_visible(self, selector: str, timeout: int = 3_000) -> bool:
        try:
            self.page.locator(selector).wait_for(state="visible", timeout=timeout)
            return True
        except PlaywrightTimeoutError:
            return False

    def is_element_present(self, selector: str) -> bool:
        return self.page.locator(selector).count() > 0

    def get_attribute(
        self, selector: str, attribute: str, timeout: int = DEFAULT_TIMEOUT
    ) -> Optional[str]:
        return self.wait_for_element(selector, timeout).get_attribute(attribute)

    def count_elements(self, selector: str) -> int:
        return self.page.locator(selector).count()

    def get_all_texts(self, selector: str) -> list[str]:
        """Return inner text of all matching elements."""
        return self.page.locator(selector).all_inner_texts()

    # ------------------------------------------------------------------
    # Screenshot
    # ------------------------------------------------------------------

    def take_screenshot(self, name: str) -> str:
        """
        Capture a full-page screenshot.
        Returns the absolute path to the saved file.
        """
        path = SCREENSHOTS_DIR / f"{name}.png"
        self.page.screenshot(path=str(path), full_page=True)
        return str(path)

    # ------------------------------------------------------------------
    # Assertions (thin wrappers around Playwright `expect`)
    # ------------------------------------------------------------------

    def assert_url_contains(self, substring: str) -> None:
        expect(self.page).to_have_url(f"**{substring}**")

    def assert_title_contains(self, substring: str) -> None:
        expect(self.page).to_have_title(f"*{substring}*")

    def assert_element_visible(
        self, selector: str, timeout: int = DEFAULT_TIMEOUT
    ) -> None:
        expect(self.page.locator(selector)).to_be_visible(timeout=timeout)

    def assert_text_equals(
        self, selector: str, expected: str, timeout: int = DEFAULT_TIMEOUT
    ) -> None:
        expect(self.page.locator(selector)).to_have_text(expected, timeout=timeout)

    def assert_text_contains(
        self, selector: str, expected: str, timeout: int = DEFAULT_TIMEOUT
    ) -> None:
        expect(self.page.locator(selector)).to_contain_text(expected, timeout=timeout)
