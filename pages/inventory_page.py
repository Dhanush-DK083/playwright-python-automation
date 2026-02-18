from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.cart_page = page.locator(".shopping_cart_badge")
        self.add_to_cart_button = page.locator("button.btn_inventory")
        self.cart_icon = page.locator(".shopping_cart_link")


    def add_first_product_cart(self):
        self.add_to_cart_button.first.click()
    def get_cart_badge(self):
        return self.cart_page

    def get_first_product_button(self):
        return self.add_to_cart_button.first

    def remove_first_product(self):
        self.get_first_product_button().click()

    def get_inventory_count(self):
        return self.inventory_items.count()
    def go_to_cart(self):
        self.cart_icon.click()
