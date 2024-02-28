from playwright.sync_api import sync_playwright
from util.credentials import empty_password, empty_username, SWAG_BASE_URL, username, password
from util.page_actions import login

def test_login_failed_when_empty_username():
  with sync_playwright() as playwright:
    # given [these prerequisites]
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # when [I do this]
    login(page, SWAG_BASE_URL, empty_username, password)

    # then [I check this]
    error_message = page.text_content('.error-message-container h3')
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    print("Authentication error message displayed successfully.")
    browser.close()

def test_login_failed_when_empty_password():
  with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    login(page, SWAG_BASE_URL, empty_password, username)

    #then
    error_message = page.text_content('.error-message-container h3')
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    print("Authentication error message displayed successfully.")
    browser.close()