from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_inventory_page(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login("standard_user", "secret_sauce")
    inv = InventoryPage(page)

    assert inv.item_count() == 6

    inv.add_to_cart("Sauce Labs Bike Light")
    inv.add_to_cart("Sauce Labs Bolt T-Shirt")
    inv.remove_from_cart("Sauce Labs Bike Light")
    inv.add_to_cart("Sauce Labs Fleece Jacket")

    assert int(inv.cart_items()) == 2