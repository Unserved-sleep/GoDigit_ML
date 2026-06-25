from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

def test_cart_page(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login()
    inv = InventoryPage(page)

    inv.add_to_cart("Sauce Labs Bike Light")
    inv.add_to_cart("Sauce Labs Bolt T-Shirt")
    inv.remove_from_cart("Sauce Labs Bike Light")
    inv.add_to_cart("Sauce Labs Fleece Jacket")
    total_item = int(inv.cart_items())

    inv.open_cart_page()

    cart = CartPage(page)
    assert cart.cart_item_count() == total_item
    cart.remove_from_cart("Sauce Labs Bolt T-Shirt")

    assert int(cart.cart_items()) == total_item -1

