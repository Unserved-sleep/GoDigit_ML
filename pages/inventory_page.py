"""
pages/inventory_page.py
-----------------------
Page Object for the SauceDemo Inventory (Products) page.
URL: https://www.saucedemo.com/inventory.html
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Encapsulates all interactions with the SauceDemo inventory page."""

    # ------------------------------------------------------------------
    # Selectors
    # ------------------------------------------------------------------
    PAGE_TITLE: str = ".title"
    PRODUCT_SORT_CONTAINER: str = ".product_sort_container"
    INVENTORY_ITEMS: str = ".inventory_item"
    ITEM_NAME: str = ".inventory_item_name"
    ITEM_PRICE: str = ".inventory_item_price"
    ITEM_DESC: str = ".inventory_item_desc"
    ADD_TO_CART_BTN: str = "button[data-test^='add-to-cart']"
    REMOVE_BTN: str = "button[data-test^='remove']"
    CART_BADGE: str = ".shopping_cart_badge"
    CART_LINK: str = ".shopping_cart_link"
    BURGER_MENU: str = "#react-burger-menu-btn"
    LOGOUT_LINK: str = "#logout_sidebar_link"
    RESET_APP_LINK: str = "#reset_sidebar_link"

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def open(self) -> "InventoryPage":
        self.navigate("https://www.saucedemo.com/inventory.html")
        return self

    def sort_products(self, sort_value: str) -> "InventoryPage":
        """
        Sort products by selecting a value from the sort dropdown.
        sort_value: 'az' | 'za' | 'lohi' | 'hilo'
        """
        self.page.locator(self.PRODUCT_SORT_CONTAINER).select_option(sort_value)
        return self

    def add_item_to_cart(self, item_name: str) -> "InventoryPage":
        """
        Click the 'Add to cart' button for the product with the given name.
        Uses an XPath to find the item card by name, then its button.
        """
        item_locator = self.page.locator(self.INVENTORY_ITEMS).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=item_name)
        )
        item_locator.locator(self.ADD_TO_CART_BTN).click()
        return self

    def remove_item_from_inventory(self, item_name: str) -> "InventoryPage":
        """Click 'Remove' for an item already in cart (from inventory page)."""
        item_locator = self.page.locator(self.INVENTORY_ITEMS).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=item_name)
        )
        item_locator.locator(self.REMOVE_BTN).click()
        return self

    def open_cart(self) -> None:
        """Click the cart icon to navigate to the Cart page."""
        self.click(self.CART_LINK)

    def open_item_detail(self, item_name: str) -> None:
        """Click on a product name to open its detail page."""
        self.page.locator(self.ITEM_NAME, has_text=item_name).click()

    def logout(self) -> None:
        """Open the burger menu and click Logout."""
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)

    def reset_app_state(self) -> None:
        """Open the burger menu and click Reset App State."""
        self.click(self.BURGER_MENU)
        self.click(self.RESET_APP_LINK)

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_cart_count(self) -> int:
        """Return the number shown on the cart badge; 0 if badge not visible."""
        if not self.is_visible(self.CART_BADGE, timeout=2_000):
            return 0
        text = self.get_text(self.CART_BADGE)
        return int(text.strip())

    def get_all_product_names(self) -> list[str]:
        return self.get_all_texts(self.ITEM_NAME)

    def get_all_product_prices(self) -> list[float]:
        raw = self.get_all_texts(self.ITEM_PRICE)
        return [float(p.replace("$", "")) for p in raw]

    def get_product_count(self) -> int:
        return self.count_elements(self.INVENTORY_ITEMS)

    def is_add_to_cart_button_visible(self, item_name: str) -> bool:
        item_locator = self.page.locator(self.INVENTORY_ITEMS).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=item_name)
        )
        return item_locator.locator(self.ADD_TO_CART_BTN).is_visible()

    def is_remove_button_visible(self, item_name: str) -> bool:
        item_locator = self.page.locator(self.INVENTORY_ITEMS).filter(
            has=self.page.locator(self.ITEM_NAME, has_text=item_name)
        )
        return item_locator.locator(self.REMOVE_BTN).is_visible()
