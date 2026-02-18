from playwright.sync_api import expect

from pages.Checkout_page import CheckoutPage
from pages.cart_page import cartPage
from pages.inventory_page import InventoryPage


def test_complete_checkout(login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_first_product_cart()
    inventory_page.go_to_cart()

    cart_page= cartPage(login_page.page)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(login_page.page)
    checkout_page.fill_information("dk", "tester", "560026")
    checkout_page.continue_button.click()
    checkout_page.finish.click()

    expect(checkout_page.success_message).to_have_text("Thank you for your order!")
