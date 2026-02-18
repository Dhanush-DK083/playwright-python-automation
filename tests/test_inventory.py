from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


def test_add_product_to_cart(login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_first_product_cart()


    expect(inventory_page.get_cart_badge()).to_be_visible()
    expect(inventory_page.get_cart_badge()).to_have_text("1")

