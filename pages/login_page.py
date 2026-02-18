from playwright.sync_api import Page


class LoginPage:
    def __init__(self,page:Page ):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_button = page.locator("[data-test='error']")
        self.error_message = page.locator("[data-test='error']")

    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username:str, password:str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()