from pages import inventory_page
from pages.inventory_page import InventoryPage


def test_inventory_item_count(login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(login_page.page)

    count = inventory_page.get_inventory_count()

    assert count ==6
