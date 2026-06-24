"""
tests/test_add_to_cart.py
--------------------------
Test suite for SauceDemo add-to-cart functionality.

Covers:
  - Add single item to cart               [smoke]
  - Add multiple items to cart            [smoke]
  - Remove item from inventory page       [regression]
  - Cart badge count reflects adds        [regression]
  - Sort products by price low→high       [regression]
  - Sort products by price high→low       [regression]
  - Sort products name A→Z               [regression]
  - Sort products name Z→A               [regression]
  - Cart persists after navigation        [regression]
"""

import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data import Products, SortOptions


class TestAddToCart:
    """Test class for SauceDemo add-to-cart and product listing scenarios."""

    # ------------------------------------------------------------------
    # Smoke tests
    # ------------------------------------------------------------------

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_add_single_item_to_cart(self, inventory_page: InventoryPage):
        """Adding one item should increment the cart badge to 1."""
        inventory_page.add_item_to_cart(Products.BACKPACK)

        assert inventory_page.get_cart_count() == 1, (
            "Cart badge should show 1 after adding one item."
        )

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_add_multiple_items_to_cart(self, inventory_page: InventoryPage):
        """Adding multiple items should reflect correct cart count."""
        items = [Products.BACKPACK, Products.BIKE_LIGHT, Products.BOLT_T_SHIRT]
        for item in items:
            inventory_page.add_item_to_cart(item)

        assert inventory_page.get_cart_count() == len(items), (
            f"Cart badge should show {len(items)} after adding {len(items)} items."
        )

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_added_item_appears_in_cart(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Added item should be present in the cart page."""
        inventory_page.add_item_to_cart(Products.FLEECE_JACKET)
        inventory_page.open_cart()

        cart = CartPage(logged_in_page)
        assert cart.is_item_in_cart(Products.FLEECE_JACKET), (
            f"'{Products.FLEECE_JACKET}' should be visible in the cart."
        )

    # ------------------------------------------------------------------
    # Regression tests
    # ------------------------------------------------------------------

    @pytest.mark.regression
    @pytest.mark.cart
    def test_remove_item_from_inventory_page(self, inventory_page: InventoryPage):
        """Adding then removing an item should decrement the cart badge back to 0."""
        inventory_page.add_item_to_cart(Products.ONESIE)
        assert inventory_page.get_cart_count() == 1

        inventory_page.remove_item_from_inventory(Products.ONESIE)
        assert inventory_page.get_cart_count() == 0, (
            "Cart badge should show 0 after removing the only item."
        )

    @pytest.mark.regression
    @pytest.mark.cart
    def test_cart_badge_count_reflects_multiple_adds(
        self, inventory_page: InventoryPage
    ):
        """Cart badge should accurately count each add."""
        for i, item in enumerate(Products.ALL, start=1):
            inventory_page.add_item_to_cart(item)
            assert inventory_page.get_cart_count() == i, (
                f"Cart count mismatch after adding item #{i}."
            )

    @pytest.mark.regression
    @pytest.mark.cart
    def test_add_to_cart_button_changes_to_remove(self, inventory_page: InventoryPage):
        """After adding an item, the button should change to 'Remove'."""
        assert inventory_page.is_add_to_cart_button_visible(Products.BACKPACK), (
            "Add to cart button should be visible initially."
        )
        inventory_page.add_item_to_cart(Products.BACKPACK)
        assert inventory_page.is_remove_button_visible(Products.BACKPACK), (
            "Remove button should appear after adding to cart."
        )

    @pytest.mark.regression
    @pytest.mark.cart
    def test_sort_products_price_low_to_high(self, inventory_page: InventoryPage):
        """Products sorted low→high should have prices in ascending order."""
        inventory_page.sort_products(SortOptions.PRICE_LOW_TO_HIGH)
        prices = inventory_page.get_all_product_prices()

        assert prices == sorted(prices), (
            f"Prices are not sorted low→high: {prices}"
        )

    @pytest.mark.regression
    @pytest.mark.cart
    def test_sort_products_price_high_to_low(self, inventory_page: InventoryPage):
        """Products sorted high→low should have prices in descending order."""
        inventory_page.sort_products(SortOptions.PRICE_HIGH_TO_LOW)
        prices = inventory_page.get_all_product_prices()

        assert prices == sorted(prices, reverse=True), (
            f"Prices are not sorted high→low: {prices}"
        )

    @pytest.mark.regression
    @pytest.mark.cart
    def test_sort_products_name_a_to_z(self, inventory_page: InventoryPage):
        """Products sorted A→Z should have names in alphabetical order."""
        inventory_page.sort_products(SortOptions.NAME_A_TO_Z)
        names = inventory_page.get_all_product_names()

        assert names == sorted(names), (
            f"Product names are not sorted A→Z: {names}"
        )

    @pytest.mark.regression
    @pytest.mark.cart
    def test_sort_products_name_z_to_a(self, inventory_page: InventoryPage):
        """Products sorted Z→A should have names in reverse alphabetical order."""
        inventory_page.sort_products(SortOptions.NAME_Z_TO_A)
        names = inventory_page.get_all_product_names()

        assert names == sorted(names, reverse=True), (
            f"Product names are not sorted Z→A: {names}"
        )

    @pytest.mark.regression
    @pytest.mark.cart
    def test_inventory_shows_six_products(self, inventory_page: InventoryPage):
        """The inventory page should always display exactly 6 products."""
        count = inventory_page.get_product_count()
        assert count == 6, f"Expected 6 products, found {count}."

    @pytest.mark.regression
    @pytest.mark.cart
    def test_remove_item_from_cart_page(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Adding an item and then removing it from the cart page should empty the cart."""
        inventory_page.add_item_to_cart(Products.RED_T_SHIRT)
        inventory_page.open_cart()

        cart = CartPage(logged_in_page)
        assert not cart.is_cart_empty(), "Cart should have one item."
        cart.remove_item(Products.RED_T_SHIRT)
        assert cart.is_cart_empty(), "Cart should be empty after removing the item."
