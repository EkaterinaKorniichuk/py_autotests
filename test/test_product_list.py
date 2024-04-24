from playwright.sync_api import sync_playwright, Page
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from util.credentials import username, incorrect_username, password, SWAG_BASE_URL, Inventory_URL
from util.page_actions import login
from util.LoginPage import LoginPage
from util.HomePage import HomePage

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

def test_verifying_that_the_all_items_section_opens_when_clicked(browser):
    # given
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.goto_login_page("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.verify_page_title("Swag Labs")
    home_page.verify_all_products_displayed()

    # when
    page.click('.bm-burger-button')
    page.click('.bm-item.menu-item')

    # then
    assert "Swag Labs" in page.title()
    assert page.query_selector('.inventory_list') is not None


def test_verifying_that_the_About_section_opens_when_clicked():
    with sync_playwright() as playwright:
        # given
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto_login_page("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        home_page = HomePage(page)
        home_page.verify_page_title("Swag Labs")
        home_page.verify_all_products_displayed()

        # when
        page.click('.bm-burger-button')
        page.click('.bm-item.menu-item[href="https://saucelabs.com/"]')

        # then
        assert "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing" in page.title()
        assert page.query_selector('h1').inner_text() == 'Website and mobile testing\nat every stage of development'
        assert page.url == "https://saucelabs.com/"
        browser.close()


