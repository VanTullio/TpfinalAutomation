import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
import time

def test_checkout_process(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(4)
    
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    time.sleep(10)
    cart.go_to_checkout()
    time.sleep(10)
    
    assert checkout.is_at_page()