from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    page.goto("https://playwright.dev")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Get started").click()
    expect(page).to_have_url("https://playwright.dev/docs/intro")

def test_saucedemo_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator(".inventory_list")).to_be_visible()

