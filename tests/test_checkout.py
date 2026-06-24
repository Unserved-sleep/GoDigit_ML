"""
tests/test_checkout.py
-----------------------
Test suite for SauceDemo checkout flow.

Covers:
  - Full happy-path checkout               [smoke, checkout]
  - Missing first name validation          [regression, checkout]
  - Missing last name validation           [regression, checkout]
  - Missing zip code validation            [regression, checkout]
  - Cancel from checkout info page         [regression, checkout]
  - Cancel from checkout overview page     [regression, checkout]
  - Order total matches expected amount    [regression, checkout]
  - Multiple items checkout flow           [regression, checkout]
"""

import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import (
    Products,
    CheckoutInfo,
    PageText,
)


class TestCheckout:
    """Test class for the SauceDemo end-to-end checkout flow."""

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _add_items_and_go_to_checkout(
        inventory_page: InventoryPage,
        logged_in_page,
        *item_names: str,
    ) -> CheckoutPage:
        """
        Add the given items to the cart, navigate to checkout step-one.
        Returns a CheckoutPage instance.
        """
        for item in item_names:
            inventory_page.add_item_to_cart(item)
        inventory_page.open_cart()
        cart = CartPage(logged_in_page)
        cart.proceed_to_checkout()
        return CheckoutPage(logged_in_page)

    # ------------------------------------------------------------------
    # Smoke tests
    # ------------------------------------------------------------------

    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_full_checkout_happy_path(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """
        Complete end-to-end checkout:
        Add item → Cart → Checkout info → Overview → Confirm → Complete screen.
        """
        # 1. Add item & navigate to checkout step 1
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.BACKPACK
        )
        assert "checkout-step-one" in checkout.get_current_url()

        # 2. Fill personal info and continue
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()
        assert "checkout-step-two" in checkout.get_current_url()

        # 3. Verify item is in overview
        assert Products.BACKPACK in checkout.get_overview_item_names()

        # 4. Finish order
        checkout.finish_checkout()
        assert checkout.is_order_complete(), (
            f"Expected to be on checkout complete, got: {checkout.get_current_url()}"
        )

        # 5. Confirm the thank-you message
        confirmation = checkout.get_order_confirmation()
        assert PageText.ORDER_COMPLETE in confirmation, (
            f"Unexpected confirmation text: '{confirmation}'"
        )

    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_checkout_page_title_step_one(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Checkout step-one page title should read 'Checkout: Your Information'."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.BIKE_LIGHT
        )
        assert checkout.get_page_title() == PageText.CHECKOUT_TITLE

    # ------------------------------------------------------------------
    # Regression tests
    # ------------------------------------------------------------------

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_missing_first_name_shows_error(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Submitting checkout info with empty first name must show validation error."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.ONESIE
        )
        info = CheckoutInfo.MISSING_FIRST
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()

        assert checkout.is_error_displayed(), "Validation error should be shown."
        assert "First Name is required" in checkout.get_error_message()

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_missing_last_name_shows_error(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Submitting with empty last name should show a validation error."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.ONESIE
        )
        info = CheckoutInfo.MISSING_LAST
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()

        assert checkout.is_error_displayed()
        assert "Last Name is required" in checkout.get_error_message()

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_missing_zip_code_shows_error(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Submitting with empty zip code should show a validation error."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.ONESIE
        )
        info = CheckoutInfo.MISSING_ZIP
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()

        assert checkout.is_error_displayed()
        assert "Postal Code is required" in checkout.get_error_message()

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_cancel_from_checkout_step_one_returns_to_cart(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Clicking Cancel on checkout info should return the user to the cart."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.BOLT_T_SHIRT
        )
        checkout.cancel_checkout()

        assert "cart" in checkout.get_current_url(), (
            "Cancel from step-one should go back to the cart page."
        )

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_cancel_from_checkout_overview_returns_to_inventory(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """Clicking Cancel on the overview step should return to the inventory page."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.FLEECE_JACKET
        )
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()

        # Now on step-two: cancel should navigate to inventory
        checkout.cancel_from_overview()
        assert "inventory" in checkout.get_current_url(), (
            "Cancel from step-two should return to the inventory page."
        )

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_order_total_calculation(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """
        The order total on the overview page should equal item total + tax.
        (Rounded to 2 decimal places to avoid floating-point issues.)
        """
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.BACKPACK, Products.BIKE_LIGHT
        )
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()

        item_total = checkout.get_item_total()
        tax = checkout.get_tax()
        displayed_total = checkout.get_total()

        expected_total = round(item_total + tax, 2)
        assert displayed_total == expected_total, (
            f"Total mismatch: item_total={item_total} + tax={tax} = "
            f"{expected_total}, but displayed {displayed_total}."
        )

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_multiple_items_appear_in_overview(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """All added items should appear on the checkout overview page."""
        items_to_add = [Products.BACKPACK, Products.BOLT_T_SHIRT, Products.ONESIE]
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, *items_to_add
        )
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()

        overview_items = checkout.get_overview_item_names()
        for item in items_to_add:
            assert item in overview_items, (
                f"'{item}' should appear in the checkout overview."
            )

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_back_home_after_order_complete(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """'Back Home' button after order complete should return to inventory."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.RED_T_SHIRT
        )
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()
        checkout.finish_checkout()

        assert checkout.is_order_complete()
        checkout.back_to_products()
        assert "inventory" in checkout.get_current_url(), (
            "Should return to inventory after clicking 'Back Home'."
        )

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_overview_page_title(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """The overview page title should read 'Checkout: Overview'."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.BIKE_LIGHT
        )
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()

        assert checkout.get_page_title() == PageText.OVERVIEW_TITLE

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_complete_page_title(
        self, inventory_page: InventoryPage, logged_in_page
    ):
        """The complete page title should read 'Checkout: Complete!'."""
        checkout = self._add_items_and_go_to_checkout(
            inventory_page, logged_in_page, Products.ONESIE
        )
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["zip_code"])
        checkout.continue_checkout()
        checkout.finish_checkout()

        assert checkout.get_page_title() == PageText.COMPLETE_TITLE
