from playwright.sync_api import Page, expect

def test_login_with_get_by_role(page: Page):
    # Using role-based locators where possible
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("UserName").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()

def test_product_list_loaded(page: Page):
    # Login first, then check inventory
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Check multiple things on the inventory page
    expect(page.locator(".inventory_list")).to_be_visible()
    expect(page.locator(".inventory_item")).to_have_count(6)

def test_add_item_to_cart(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Add first item to cart
    page.locator(".btn_inventory").first.click()

    # Cart badge should now show 1
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

def test_product_sort_dropdown(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Interact with dropdown
    page.locator(".product_sort_container").select_option("za")
    first_item = page.locator(".inventory_item_name").first
    expect(first_item).to_have_text("Test.allTheThings() T-Shirt (Red)")
