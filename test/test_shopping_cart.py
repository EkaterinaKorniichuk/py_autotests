from playwright.sync_api import sync_playwright
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.credentials import username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login
from util.page_actions import add_product_to_cart


def test_shopping_cart_item_add_from_main_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)


        # when
        page.get_by_text('Sauce Labs Backpack');
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


def test_shopping_cart_item_successful_add_from_prodpage():
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
        add_product_to_cart(page, 'Sauce Labs Backpack')
        add_product_to_cart(page, 'Sauce Labs Bike Light')

        # when
        page.goto(Inventory_URL)
        product = page.get_by_text('Sauce Labs Backpack')
        product.click()
        remove_button = page.wait_for_selector('.btn_secondary.btn_inventory')
        remove_button.click()

        # then
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'

        cart_item = page.query_selector('.cart_item')
        assert cart_item.inner_text().find('Sauce Labs Backpack') == -1
        assert cart_item.inner_text().find('Sauce Labs Bike Light') != -1

        browser.close()

def test_removing_product_from_the_shopping_cart_from_products_main_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        inventory_items = page.query_selector_all('.inventory_item')

        # for item in inventory_items:
        #     item_name_element = item.query_selector('.inventory_item_name')
        #     item_name = item_name_element.inner_text()
        #     if item_name == 'Sauce Labs Backpack':
        #         add_to_cart_button = item.query_selector('.btn_inventory')
        #         add_to_cart_button.click()
        #         remove_button = item.query_selector('.btn_secondary.btn_inventory')
        #         remove_button.click()
        #
        #         break

        # when
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()

        # then
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'
        cart_item = page.query_selector('.cart_item')
        assert cart_item is None or cart_item.inner_text().find('Sauce Labs Backpack') == -1

        browser.close()


def test_add_two_items_in_shopping_cart_from_main_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)

        # when
        add_product_to_cart(page, 'Sauce Labs Backpack')
        add_product_to_cart(page, 'Sauce Labs Bike Light')

        # then
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()


        browser.close()




def test_return_to_cart_after_browser_close():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        add_to_cart_button = page.wait_for_selector('.btn_inventory')
        add_to_cart_button.click()

        # when
        page.close()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/cart.html")

        # then
        assert page.wait_for_selector('.btn_secondary.btn_medium').inner_text() == 'Continue Shopping'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Checkout'
        assert page.query_selector('.inventory_item_name').inner_text() == 'Sauce Labs Backpack'

        browser.close()

def test_checkout_page_is_displayed_correclty():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        add_product_to_cart(page, 'Sauce Labs Backpack')
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.query_selector('.cart_item') is not None

        # when
        checkout_button = page.wait_for_selector('.btn_action.btn_medium')
        checkout_button.click()

        # then
        assert "Swag Labs" in page.title()
        assert page.query_selector('input[name="firstName"]') is not None
        assert page.query_selector('input[name="lastName"]') is not None
        assert page.query_selector('input[name="postalCode"]') is not None
        assert page.query_selector('.cart_cancel_link.btn_secondary') is not None
        assert page.query_selector('.btn_primary.cart_button') is not None

        page.close()
        context.close()
        browser.close()



def test_fill_the_checkout_your_information_form_with_valid_data():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        add_product_to_cart(page, 'Sauce Labs Backpack')
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.query_selector('.cart_item') is not None
        checkout_button = page.wait_for_selector('.btn_action.btn_medium')
        checkout_button.click()

        # when
        page.fill('#first-name', 'Katya')
        page.fill('#last-name', 'Korniichuk')
        page.fill('#postal-code', '92122')
        continue_button = page.wait_for_selector('.cart_button')
        continue_button.click()

        # then
        assert page.wait_for_selector('div.inventory_item_name').inner_text() == 'Sauce Labs Backpack'
        assert page.wait_for_selector('div.inventory_item_desc').inner_text() == 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.'
        assert page.wait_for_selector('div.inventory_item_price').inner_text() == '$29.99'
        assert page.wait_for_selector('.btn_secondary.back.btn_medium').inner_text() == 'Cancel'
        assert page.wait_for_selector('.btn_action.btn_medium').inner_text() == 'Finish'

        page.close()
        context.close()
        browser.close()

def test_check_that_the_first_name_field_is_mandatory_on_Your_information_page():
    with sync_playwright() as playwright:
       # given
       browser = playwright.chromium.launch(headless=False, slow_mo=500)
       context = browser.new_context()
       page = context.new_page()
       login(page, SWAG_BASE_URL, username, password)
       page.goto(Inventory_URL)
       add_product_to_cart(page, 'Sauce Labs Backpack')
       shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
       shopping_cart_icon.click()
       assert page.query_selector('.cart_item') is not None
       checkout_button = page.wait_for_selector('.btn_action.btn_medium')
       checkout_button.click()

       # when
       page.fill('#last-name', 'Korniichuk')
       page.fill('#postal-code', '92122')
       continue_button = page.wait_for_selector('.cart_button')
       continue_button.click()

       # then
       error_message = page.wait_for_selector('.error-message-container h3')
       assert error_message.inner_text() == 'Error: First Name is required'

       page.close()
       context.close()
       browser.close()

def test_check_that_the_last_name_field_is_mandatory_on_Your_information_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        add_product_to_cart(page, 'Sauce Labs Backpack')
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.query_selector('.cart_item') is not None
        checkout_button = page.wait_for_selector('.btn_action.btn_medium')
        checkout_button.click()

        # when
        page.fill('#first-name', 'Katya')
        page.fill('#postal-code', '92122')
        continue_button = page.wait_for_selector('.cart_button')
        continue_button.click()

        # then
        error_message = page.wait_for_selector('.error-message-container h3')
        assert error_message.inner_text() == 'Error: Last Name is required'

        page.close()
        context.close()
        browser.close()

def test_check_zip_code_field_is_mandatory_on_Your_information_page():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        add_product_to_cart(page, 'Sauce Labs Backpack')
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.query_selector('.cart_item') is not None
        checkout_button = page.wait_for_selector('.btn_action.btn_medium')
        checkout_button.click()

        # when
        page.fill('#first-name', 'Katya')
        page.fill('#last-name', 'Korniichuk')
        continue_button = page.wait_for_selector('.cart_button')
        continue_button.click()

        # then
        error_message = page.wait_for_selector('.error-message-container h3')
        assert error_message.inner_text() == 'Error: Postal Code is required'

        page.close()
        context.close()
        browser.close()




def test_finish_page_is_displayed_correctly():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        login(page, SWAG_BASE_URL, username, password)
        page.goto(Inventory_URL)
        add_product_to_cart(page, 'Sauce Labs Backpack')
        shopping_cart_icon = page.wait_for_selector('.shopping_cart_container')
        shopping_cart_icon.click()
        assert page.query_selector('.cart_item') is not None
        checkout_button = page.wait_for_selector('.btn_action.btn_medium')
        checkout_button.click()
        page.fill('#first-name', 'Katya')
        page.fill('#last-name', 'Korniichuk')
        page.fill('#postal-code', '92122')
        continue_button = page.wait_for_selector('.cart_button')
        continue_button.click()

        # when
        finish_button = page.wait_for_selector('.btn_action.btn_medium')
        finish_button.click()

        # then
        assert page.wait_for_selector('.complete-header').inner_text() == 'Thank you for your order!'
        assert page.wait_for_selector('.complete-text').inner_text() == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        assert page.wait_for_selector('.btn_primary').inner_text() == 'Back Home'

        page.close()
        context.close()
        browser.close()


