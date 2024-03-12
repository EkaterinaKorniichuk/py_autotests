from playwright.sync_api import sync_playwright
from util.credentials import username, incorrect_username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login


def test_product_list_valid_сredentials():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # when
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # then
        assert page.url == 'https://www.saucedemo.com/inventory.html'
        assert page.inner_text('.inventory_item') != ''

        browser.close()

def test_product_list_invalid_credentials():
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
        prices = page.query_selector_all('.inventory_item_price')
        product_prices = [float(price.inner_text().replace('$', '')) for price in prices]
        assert product_prices == sorted(product_prices)

        browser.close()

def test_sorting_product_hilo():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)

        # when
        page.goto(Inventory_URL)
        dropdown_button = page.wait_for_selector('.product_sort_container')
        dropdown_button.click()
        dropdown_button.select_option(label='Price (high to low)')

        # then
        prices = page.query_selector_all('.inventory_item_price')
        product_prices = [float(price.inner_text().replace('$', '')) for price in prices]
        assert product_prices == sorted(product_prices, reverse=True)

        browser.close()


def test_product_page_displays_correctly():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # when
        product = page.get_by_text('Sauce Labs Backpack')
        product.click()

        # then
        assert page.wait_for_selector('div.inventory_details_name').inner_text() == 'Sauce Labs Backpack'
        assert page.wait_for_selector('div.inventory_details_price').inner_text() == '$29.99'
        assert page.wait_for_selector('.btn_inventory').inner_text().upper() == 'ADD TO CART'
        assert page.wait_for_selector('.shopping_cart_container').is_visible()
        assert page.wait_for_selector('.header_secondary_container').inner_text() == 'Back to products'


        browser.close()

