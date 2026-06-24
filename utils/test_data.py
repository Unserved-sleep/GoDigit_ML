"""
utils/test_data.py
------------------
Centralized test data and credentials for the SauceDemo test suite.
All usernames and passwords come from: https://www.saucedemo.com
"""

# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------
STANDARD_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}

LOCKED_OUT_USER = {
    "username": "locked_out_user",
    "password": "secret_sauce",
}

PROBLEM_USER = {
    "username": "problem_user",
    "password": "secret_sauce",
}

PERFORMANCE_GLITCH_USER = {
    "username": "performance_glitch_user",
    "password": "secret_sauce",
}

ERROR_USER = {
    "username": "error_user",
    "password": "secret_sauce",
}

VISUAL_USER = {
    "username": "visual_user",
    "password": "secret_sauce",
}

INVALID_USER = {
    "username": "invalid_user",
    "password": "wrong_password",
}

# ---------------------------------------------------------------------------
# Expected error messages
# ---------------------------------------------------------------------------
class ErrorMessages:
    LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    INVALID_CREDENTIALS = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    USERNAME_REQUIRED = "Epic sadface: Username is required"
    PASSWORD_REQUIRED = "Epic sadface: Password is required"


# ---------------------------------------------------------------------------
# Product data
# ---------------------------------------------------------------------------
class Products:
    BACKPACK = "Sauce Labs Backpack"
    BIKE_LIGHT = "Sauce Labs Bike Light"
    BOLT_T_SHIRT = "Sauce Labs Bolt T-Shirt"
    FLEECE_JACKET = "Sauce Labs Fleece Jacket"
    ONESIE = "Sauce Labs Onesie"
    RED_T_SHIRT = "Test.allTheThings() T-Shirt (Red)"

    ALL = [BACKPACK, BIKE_LIGHT, BOLT_T_SHIRT, FLEECE_JACKET, ONESIE, RED_T_SHIRT]

    PRICES = {
        BACKPACK: 29.99,
        BIKE_LIGHT: 9.99,
        BOLT_T_SHIRT: 15.99,
        FLEECE_JACKET: 49.99,
        ONESIE: 7.99,
        RED_T_SHIRT: 15.99,
    }


# ---------------------------------------------------------------------------
# Sort options
# ---------------------------------------------------------------------------
class SortOptions:
    NAME_A_TO_Z = "az"
    NAME_Z_TO_A = "za"
    PRICE_LOW_TO_HIGH = "lohi"
    PRICE_HIGH_TO_LOW = "hilo"


# ---------------------------------------------------------------------------
# Checkout info
# ---------------------------------------------------------------------------
class CheckoutInfo:
    VALID = {
        "first_name": "John",
        "last_name": "Doe",
        "zip_code": "12345",
    }
    MISSING_FIRST = {
        "first_name": "",
        "last_name": "Doe",
        "zip_code": "12345",
    }
    MISSING_LAST = {
        "first_name": "Jane",
        "last_name": "",
        "zip_code": "10001",
    }
    MISSING_ZIP = {
        "first_name": "Jane",
        "last_name": "Doe",
        "zip_code": "",
    }


# ---------------------------------------------------------------------------
# URLs
# ---------------------------------------------------------------------------
class URLs:
    BASE = "https://www.saucedemo.com"
    INVENTORY = "/inventory.html"
    CART = "/cart.html"
    CHECKOUT_STEP_ONE = "/checkout-step-one.html"
    CHECKOUT_STEP_TWO = "/checkout-step-two.html"
    CHECKOUT_COMPLETE = "/checkout-complete.html"


# ---------------------------------------------------------------------------
# Expected page text
# ---------------------------------------------------------------------------
class PageText:
    ORDER_COMPLETE = "Thank you for your order!"
    ORDER_DISPATCHED = "Your order has been dispatched"
    CHECKOUT_TITLE = "Checkout: Your Information"
    OVERVIEW_TITLE = "Checkout: Overview"
    COMPLETE_TITLE = "Checkout: Complete!"
    CART_TITLE = "Your Cart"
    PRODUCTS_TITLE = "Products"
