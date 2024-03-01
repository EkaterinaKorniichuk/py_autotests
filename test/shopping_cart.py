from playwright.sync_api import sync_playwright
from util.credentials import username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login

def test_shopping_cart_item_successful():
    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        login(page, SWAG_BASE_URL, username, password)

        page.goto(Inventory_URL)

        product = page.wait_for_selector('id="item_4_title_link"')
        product.click()

