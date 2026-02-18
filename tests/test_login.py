import re
from logging import error

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.data_reader import load_test_data

data = load_test_data("test_data/login_test_data.json")

def test_valid_login(login_page):
    credentials =data["valid_login"]


    login_page.login(credentials["username"], credentials["password"])

    expect (login_page.page).to_have_url(re.compile(r".*inventory.html"))
    expect(login_page.page.locator(".inventory_list")).to_be_visible()

@pytest.mark.parametrize("userdata", data["invalid_login"])
def test_invalid_login(login_page,userdata,):
    login_page.login(userdata["username"], userdata["password"])

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(userdata["error"])





