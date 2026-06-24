"""
pages/checkout_page.py
----------------------
Page Object for the SauceDemo Checkout flow (3 steps):
  Step 1 — Checkout: Your Information (/checkout-step-one.html)
  Step 2 — Checkout: Overview           (/checkout-step-two.html)
  Step 3 — Checkout: Complete!           (/checkout-complete.html)

All three steps are handled in a single class to model the sequential flow.
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Encapsulates all interactions across the SauceDemo checkout flow."""

    # ------------------------------------------------------------------
    # Selectors — Step 1: Information
    # ------------------------------------------------------------------
    FIRST_NAME_INPUT: str = "#first-name"
    LAST_NAME_INPUT: str = "#last-name"
    ZIP_CODE_INPUT: str = "#postal-code"
    CONTINUE_BTN: str = "#continue"
    CANCEL_BTN: str = "#cancel"
    ERROR_MESSAGE: str = "[data-test='error']"
    ERROR_CLOSE_BTN: str = ".error-button"

    # ------------------------------------------------------------------
    # Selectors — Step 2: Overview
    # ------------------------------------------------------------------
    FINISH_BTN: str = "#finish"
    SUMMARY_ITEM_TOTAL: str = ".summary_subtotal_label"
    SUMMARY_TAX: str = ".summary_tax_label"
    SUMMARY_TOTAL: str = ".summary_total_label"
    OVERVIEW_ITEMS: str = ".cart_item"
    ITEM_NAME: str = ".inventory_item_name"
    ITEM_PRICE: str = ".inventory_item_price"
    PAYMENT_INFO: str = ".summary_value_label"

    # ------------------------------------------------------------------
    # Selectors — Step 3: Complete
    # ------------------------------------------------------------------
    COMPLETE_HEADER: str = ".complete-header"
    COMPLETE_TEXT: str = ".complete-text"
    BACK_HOME_BTN: str = "#back-to-products"
    PONY_EXPRESS_IMG: str = ".pony_express"

    # ------------------------------------------------------------------
    # Selectors — Shared
    # ------------------------------------------------------------------
    PAGE_TITLE: str = ".title"

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # ------------------------------------------------------------------
    # Actions — Step 1
    # ------------------------------------------------------------------

    def open_step_one(self) -> "CheckoutPage":
        self.navigate("https://www.saucedemo.com/checkout-step-one.html")
        return self

    def enter_first_name(self, first_name: str) -> "CheckoutPage":
        self.fill(self.FIRST_NAME_INPUT, first_name)
        return self

    def enter_last_name(self, last_name: str) -> "CheckoutPage":
        self.fill(self.LAST_NAME_INPUT, last_name)
        return self

    def enter_zip_code(self, zip_code: str) -> "CheckoutPage":
        self.fill(self.ZIP_CODE_INPUT, zip_code)
        return self

    def fill_info(
        self, first_name: str, last_name: str, zip_code: str
    ) -> "CheckoutPage":
        """Fill all checkout information fields."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        return self

    def continue_checkout(self) -> None:
        """Click 'Continue' to proceed to the overview step."""
        self.click(self.CONTINUE_BTN)

    def cancel_checkout(self) -> None:
        """Click 'Cancel' to abort checkout."""
        self.click(self.CANCEL_BTN)

    def close_error(self) -> None:
        if self.is_visible(self.ERROR_CLOSE_BTN):
            self.click(self.ERROR_CLOSE_BTN)

    # ------------------------------------------------------------------
    # Actions — Step 2
    # ------------------------------------------------------------------

    def finish_checkout(self) -> None:
        """Click 'Finish' to complete the order."""
        self.click(self.FINISH_BTN)

    def cancel_from_overview(self) -> None:
        """Click 'Cancel' on the overview step (returns to cart)."""
        self.click(self.CANCEL_BTN)

    # ------------------------------------------------------------------
    # Actions — Step 3
    # ------------------------------------------------------------------

    def back_to_products(self) -> None:
        """Click 'Back Home' to return to the inventory page."""
        self.click(self.BACK_HOME_BTN)

    # ------------------------------------------------------------------
    # Queries — Step 1
    # ------------------------------------------------------------------

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    # ------------------------------------------------------------------
    # Queries — Step 2
    # ------------------------------------------------------------------

    def get_item_total(self) -> float:
        """
        Parse and return the item subtotal (before tax).
        Example label: "Item total: $29.99"
        """
        raw = self.get_text(self.SUMMARY_ITEM_TOTAL)
        return float(raw.split("$")[-1])

    def get_tax(self) -> float:
        raw = self.get_text(self.SUMMARY_TAX)
        return float(raw.split("$")[-1])

    def get_total(self) -> float:
        raw = self.get_text(self.SUMMARY_TOTAL)
        return float(raw.split("$")[-1])

    def get_overview_item_names(self) -> list[str]:
        return self.get_all_texts(self.ITEM_NAME)

    def get_overview_item_prices(self) -> list[float]:
        raw = self.get_all_texts(self.ITEM_PRICE)
        return [float(p.replace("$", "")) for p in raw]

    def get_overview_item_count(self) -> int:
        return self.count_elements(self.OVERVIEW_ITEMS)

    # ------------------------------------------------------------------
    # Queries — Step 3
    # ------------------------------------------------------------------

    def get_order_confirmation(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self) -> str:
        return self.get_text(self.COMPLETE_TEXT)

    def is_order_complete(self) -> bool:
        return "complete" in self.get_current_url()

    # ------------------------------------------------------------------
    # Queries — Shared
    # ------------------------------------------------------------------

    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)
