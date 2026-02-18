import pytest

from pages.login_page import LoginPage
from utils.data_reader import load_test_data

@pytest.fixture
def login_page(page):
    login =LoginPage(page)
    login.load()
    return login