# page_actions.py
from util.credentials import Inventory_URL


def login(page, SWAG_BASE_URL, username, password):
    page.goto(SWAG_BASE_URL)
    page.fill('input[name="user-name"]', username)
    page.fill('input[name="password"]', password)
    page.click('input[type="submit"]')
    page.wait_for_load_state()


def add_product_to_cart(page, product_name):
    initial_page = page.url

    page.goto(Inventory_URL)
    product = page.get_by_text(product_name)
    product.click()

    add_to_cart_button = page.wait_for_selector('.btn_inventory')
    add_to_cart_button.click()

    page.goto(initial_page)

def add_product_to_cart_from_all_products(page, product_name):
    page.goto(Inventory_URL)
    product = page.query_selector(f'.inventory_item_label:has-text("{product_name}")')
    product.click()
    add_to_cart_button = page.wait_for_selector('.btn_inventory')
    add_to_cart_button.click()
