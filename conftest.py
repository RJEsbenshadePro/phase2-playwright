import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture
def logged_in_page(page: Page):
    """Logs into SauceDemo and returns the page ready to use."""
    page.goto(BASE_URL)
    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    # Wait until we're actually on the inventory page before handing off
    page.wait_for_url("**/inventory.html")
    return page