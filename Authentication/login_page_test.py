from playwright.sync_api import sync_playwright
from util.credentials import SWAG_BASE_URL

def test_login_page():
 with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch()
    # Create a new page
    page = browser.new_page()
    # Visit the Swag_Labs website
    page.goto(SWAG_BASE_URL)

    #Check the page title
    page_title = page.text_content("login_logo")
    assert page_title == "Swag Labs"

    #Ckeck "Login" button
    login_button = page.wait_for_selector("#login-button")
    assert login_button is not None


    browser.close()

test_login_page()