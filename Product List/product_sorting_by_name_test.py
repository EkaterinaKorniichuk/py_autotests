from playwright.sync_api import sync_playwright
from util.credentials import username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login

def test_sorting_product_az():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)

        select_container = page.locator("button#product_sort_container")


        #page.locator("div.right_component").highlight()
        #page.locator("div.right_component:visible").highlight()
        #page.locator("div.right_component:visible a:text('Name (A to Z')").highlight()

        dropdown_button = page.wait_for_selector('.product_sort_container')
        dropdown_button.click()

        option_name_az = page.wait_for_selector('option[value="az"]')
        option_name_az.click()







