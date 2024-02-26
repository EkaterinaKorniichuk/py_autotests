from playwright.sync_api import sync_playwright
from credentials import Inventory_URL


def test_product_list_checking():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        page.goto(Inventory_URL)

try:
    if page.inner_text('.inventory_item') != '':
        print("Product list displayed correctly")
    else:
        print("No products displayed on the screen")
except Exception as e:
    print("An error occurred:", e)
