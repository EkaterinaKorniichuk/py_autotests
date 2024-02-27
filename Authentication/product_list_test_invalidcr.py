from playwright.sync_api import sync_playwright
from credentials import incorrect_username, password, SWAG_BASE_URL, Inventory_URL
from page_actions import login

def test_product_list_():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        login(page, SWAG_BASE_URL, incorrect_username, password)

        page.goto(Inventory_URL)

        error_message = page.text_content('.error-message-container h3')
        assert "Epic sadface: You can only access '/inventory.html' when you are logged in" in error_message
        print("Authentication error message displayed successfully.")
        browser.close()

