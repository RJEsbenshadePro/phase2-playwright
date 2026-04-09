from playwright.sync_api import Page, expect

def test_inventory_page_loads(logged_in_page: Page):
    expect(logged_in_page.get_by_text("Products")).to_be_visible()
    expect(logged_in_page.locator(".inventory_item")).to_have_count(6)

def test_add_item_to_cart(logged_in_page: Page):
    logged_in_page.locator(".btn_inventory").first.click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")

def test_sort_products_low_to_high(logged_in_page: Page):
    logged_in_page.locator(".product_sort_container").select_option("lohi")
    prices = logged_in_page.locator(".inventory_item_price").all_text_contents()
    price_values = [float(p.replace("$", "")) for p in prices]
    assert price_values == sorted(price_values)

def test_product_detail_page(logged_in_page: Page):
    logged_in_page.locator(".inventory_item_name").first.click()
    expect(logged_in_page.locator(".inventory_details_name")).to_be_visible()
    expect(logged_in_page.locator("#add-to-cart")).to_be_visible()
