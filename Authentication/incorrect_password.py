from playwright.sync_api import sync_playwright
from credentials import username, incorrect_password, SWAG_BASE_URL
from page_actions import login

   # when
def test_login_successful():
 with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    login(page, SWAG_BASE_URL, incorrect_password, username)



    #then
    error_message = page.text_content('.error-message-container h3')
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    print("Authentication error message displayed successfully.")
    browser.close()