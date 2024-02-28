from playwright.sync_api import sync_playwright
from util.credentials import username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login

def test_product_list_():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        login(page, SWAG_BASE_URL, username, password)

        page.goto(Inventory_URL)

        assert page.url == 'https://www.saucedemo.com/inventory.html'
        inventory_container_text = page.inner_text('.inventory_list')
        assert page.inner_text('.inventory_item') != '', 'No products displayed on the screen'

        browser.close()



