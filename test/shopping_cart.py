from playwright.sync_api import sync_playwright
from util.credentials import username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login


def test_shopping_cart_item_successful_from_mainpage():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # when
        inventory_items = page.query_selector_all('.inventory_item')

        for item in inventory_items:
            item_name_element = item.query_selector('.inventory_item_name')
            item_name = item_name_element.inner_text()
            if item_name == 'Sauce Labs Backpack':
                add_to_cart_button = item.query_selector('.btn_inventory')
                add_to_cart_button.click()
                break

        # then
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.wait_for_selector('div.inventory_item_name').inner_text() == 'Sauce Labs Backpack'
        assert page.wait_for_selector('div.inventory_item_desc').inner_text() == 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.'
        assert page.wait_for_selector('div.inventory_item_price').inner_text() == '$29.99'
        assert page.wait_for_selector('.btn_secondary.btn_small').inner_text() == 'Remove'
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'

        browser.close()


def test_shopping_cart_item_successful_from_prodpage():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # when
        product = page.get_by_text('Sauce Labs Backpack')
        product.click()
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()

        # then
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.wait_for_selector('div.inventory_item_name').inner_text() == 'Sauce Labs Backpack'
        assert page.wait_for_selector('div.inventory_item_desc').inner_text() == 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.'
        assert page.wait_for_selector('div.inventory_item_price').inner_text() == '$29.99'
        assert page.wait_for_selector('.btn_secondary.btn_small').inner_text() == 'Remove'
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'

        browser.close()


def test_removing_product_from_the_shopping_cart_from_product_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # when
        product = page.get_by_text('Sauce Labs Backpack')
        product.click()
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()
        remove_button = page.wait_for_selector('.btn_secondary.btn_inventory')
        remove_button.click()

        # then
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'
        cart_item = page.query_selector('.cart_item')
        assert cart_item is None or cart_item.inner_text().find('Sauce Labs Backpack') == -1

        browser.close()


def test_removing_product_from_the_shopping_cart_from_products_main_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # when
        inventory_items = page.query_selector_all('.inventory_item')

        for item in inventory_items:
            item_name_element = item.query_selector('.inventory_item_name')
            item_name = item_name_element.inner_text()
            if item_name == 'Sauce Labs Backpack':
                add_to_cart_button = item.query_selector('.btn_inventory')
                add_to_cart_button.click()
                remove_button = item.query_selector('.btn_secondary.btn_inventory')
                remove_button.click()

                break

        # then
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'
        cart_item = page.query_selector('.cart_item')
        assert cart_item is None or cart_item.inner_text().find('Sauce Labs Backpack') == -1

        browser.close()


def test_changing_quantity_of_item_in_shopping_cart():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        inventory_items = page.query_selector_all('.inventory_item')

        for item in inventory_items:
            item_name_element = item.query_selector('.inventory_item_name')
            item_name = item_name_element.inner_text()
            if item_name == 'Sauce Labs Backpack':
                add_to_cart_button = item.query_selector('.btn_inventory')
                add_to_cart_button.click()
                break

        # when
        inventory_items = page.query_selector_all('.inventory_item')

        for item in inventory_items:
            item_name_element = item.query_selector('.inventory_item_name')
            item_name = item_name_element.inner_text()
            if item_name == 'Sauce Labs Bike Light':
                add_to_cart_button = item.query_selector('.btn_inventory')
                add_to_cart_button.click()
                break

        # then
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()


        browser.close()




def test_return_to_cart_after_browser_close():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()

        # when
        page.close()
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/cart.html")

        # then
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'
        assert page.query_selector('.inventory_item_name').inner_text() == 'Sauce Labs Backpack'

        browser.close()
