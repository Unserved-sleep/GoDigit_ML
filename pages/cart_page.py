"""
pages/cart_page.py
------------------
Page Object for the SauceDemo Cart page.
URL: https://www.saucedemo.com/cart.html
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """Encapsulates all interactions with the SauceDemo cart page."""

    # ------------------------------------------------------------------
    # Selectors
    # ------------------------------------------------------------------
    PAGE_TITLE: str = ".title"
    CART_ITEMS: str = ".cart_item"
    ITEM_NAME: str = ".inventory_item_name"
    ITEM_PRICE: str = ".inventory_item_price"
    ITEM_QUANTITY: str = ".cart_quantity"
    REMOVE_BTN_TEMPLATE: str = "button[data-test='remove-{slug}']"
    CONTINUE_SHOPPING_BTN: str = "#continue-shopping"
    CHECKOUT_BTN: str = "#checkout"
    CART_BADGE: str = ".shopping_cart_badge"

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def open(self) -> "CartPage":
        self.navigate("https://www.saucedemo.com/cart.html")
        return self

    def remove_item(self, item_name: str) -> "CartPage":
        """
        Remove an item from the cart by its display name.
        Finds the cart item container, then clicks its Remove button.
        """
        item_locator = self.page.locator(self.CART_ITEMS).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=item_name)
        )
        item_locator.locator("button").click()
        return self

    def proceed_to_checkout(self) -> None:
        """Click the 'Checkout' button."""
        self.click(self.CHECKOUT_BTN)

    def continue_shopping(self) -> None:
        """Click the 'Continue Shopping' button."""
        self.click(self.CONTINUE_SHOPPING_BTN)

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_cart_items(self) -> list[str]:
        """Return a list of item names currently in the cart."""
        return self.get_all_texts(self.ITEM_NAME)

    def get_cart_item_count(self) -> int:
        return self.count_elements(self.CART_ITEMS)

    def get_item_price(self, item_name: str) -> float:
        """Return the price of a specific item in the cart."""
        item_locator = self.page.locator(self.CART_ITEMS).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=item_name)
        )
        price_text = item_locator.locator(self.ITEM_PRICE).inner_text()
        return float(price_text.replace("$", ""))

    def get_item_quantity(self, item_name: str) -> int:
        """Return the quantity for a specific item."""
        item_locator = self.page.locator(self.CART_ITEMS).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=item_name)
        )
        return int(item_locator.locator(self.ITEM_QUANTITY).inner_text())

    def is_item_in_cart(self, item_name: str) -> bool:
        return item_name in self.get_cart_items()

    def is_cart_empty(self) -> bool:
        return self.get_cart_item_count() == 0

    def get_cart_badge_count(self) -> int:
        """Return the number shown on the cart badge; 0 if not visible."""
        if not self.is_visible(self.CART_BADGE, timeout=2_000):
            return 0
        return int(self.get_text(self.CART_BADGE).strip())
