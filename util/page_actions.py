# page_actions.py
from util.credentials import Inventory_URL


def login(page, SWAG_BASE_URL, username, password):
    page.goto(SWAG_BASE_URL)
    page.fill('input[name="user-name"]', username)
    page.fill('input[name="password"]', password)
    page.click('input[type="submit"]')
    page.wait_for_load_state()


def add_product_to_cart(page, product_name):
   assert isinstance(Inventory_URL, object)
   page.goto(Inventory_URL)
   product = page.get_by_text(product_name)
   product.click()
   add_to_cart_button = page.wait_for_selector('.btn_inventory')
   add_to_cart_button.click()