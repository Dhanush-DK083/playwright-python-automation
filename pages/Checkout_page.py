from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page:Page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def fill_information(self, first,last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def continue_button(self):
        self.continue_button.click()
    def finish_checkout(self):
        self.finish.click()