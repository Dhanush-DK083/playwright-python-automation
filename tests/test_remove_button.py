from playwright.sync_api import expect

from pages import inventory_page
from pages.inventory_page import InventoryPage


def test_remove_from_cart(login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_first_product_cart()


    expect(inventory_page.get_cart_badge()).to_have_text("1")

    expect(inventory_page.get_first_product_button()).to_have_text("Remove")

    inventory_page.remove_first_product()

    expect(inventory_page.get_cart_badge()).not_to_be_visible()

