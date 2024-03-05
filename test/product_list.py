from playwright.sync_api import sync_playwright
from util.credentials import username, incorrect_username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login

def test_product_list_valid():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # when
        login(page, SWAG_BASE_URL, username, password)

        # then
        page.goto(Inventory_URL)
        assert page.url == 'https://www.saucedemo.com/inventory.html'
        inventory_container_text = page.inner_text('.inventory_list')
        assert page.inner_text('.inventory_item') != '', 'No products displayed on the screen'
        browser.close()

def test_product_list_invalid():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # when
        login(page, SWAG_BASE_URL, incorrect_username, password)

        # then
        page.goto(Inventory_URL)
        error_message = page.text_content('.error-message-container h3')
        assert "Epic sadface: You can only access '/inventory.html' when you are logged in" in error_message
        print("Authentication error message displayed successfully.")
        browser.close()

def test_sorting_product_az():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        dropdown_button = page.wait_for_selector('.product_sort_container')
        dropdown_button.click()
        dropdown_button.select_option(label='Name (A to Z)')

        # then
        products = page.query_selector_all('.inventory_item_name')
        product_names = [product.text_content() for product in products]
        product_names.sort()
        assert [product.text_content() for product in products] == product_names


        browser.close()

def test_sorting_product_za():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        dropdown_button = page.wait_for_selector('.product_sort_container')
        dropdown_button.click()
        dropdown_button.select_option(label='Name (Z to A)')

        # then
        products = page.query_selector_all('.inventory_item_name')
        product_names = [product.text_content() for product in products]
        product_names.sort(reverse=True)
        assert [product.text_content() for product in products] == product_names

        browser.close()

def test_sorting_product_lohi():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        dropdown_button = page.wait_for_selector('.product_sort_container')
        dropdown_button.click()
        dropdown_button.select_option(label='Price (low to high)')

        # then
        products = page.query_selector_all('.inventory_item_name')
        product_names = [product.text_content() for product in products]
        product_names.sort()
        assert [product.text_content() for product in products] == product_names

        browser.close()

def test_sorting_product_hilo():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # when
        login(page, SWAG_BASE_URL, username, password)

        # then
        page.goto(Inventory_URL)

        dropdown_button = page.wait_for_selector('.product_sort_container')
        dropdown_button.click()
        dropdown_button.select_option(label='Price (high to low)')
        browser.close()


def test_product_page_displays_correctly():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # when
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # then
        product = page.get_by_text('Sauce Labs Backpack')
        product.click()

        browser.close()

