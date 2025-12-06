import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import time

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    
    #time.sleep(3)

    # Agregar producto e ir al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    # Verifica un producto cargado en carrito
    assert cart.get_cart_items_count() == 1