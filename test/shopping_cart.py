from playwright.sync_api import sync_playwright
from util.credentials import username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login


def test_shopping_cart_item_successful_from_mainpage():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        product = page.get_by_text('Sauce Labs Backpack')
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()

        # then
        page.goto("https://www.saucedemo.com/cart.html")

        browser.close()



def test_shopping_cart_item_successful_from_prodpage():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        product = page.get_by_text('Sauce Labs Backpack')
        product.click()
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()

        # then
        page.goto("https://www.saucedemo.com/cart.html")

        browser.close()

def test_removing_product_from_the_shopping_cart_from_product_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        product = page.get_by_text('Sauce Labs Backpack')
        product.click()
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()
        remove_button = page.wait_for_selector('.btn_secondary.btn_inventory')
        remove_button.click()

        # then
        page.goto("https://www.saucedemo.com/cart.html")
        browser.close()

def test_removing_product_from_the_shopping_cart_from_product_main_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        product = page.get_by_text('Sauce Labs Backpack')
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()
        remove_button = page.wait_for_selector('.btn_secondary.btn_inventory')
        remove_button.click()

        # then
        page.goto("https://www.saucedemo.com/cart.html")
        browser.close()


