from playwright.sync_api import sync_playwright
from util.credentials import username, password, SWAG_BASE_URL
from util.page_actions import login

def test_successful_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()


        login(page, SWAG_BASE_URL, username, password)


        page_title = page.title()
        assert page_title == "Swag Labs"
        assert page.inner_html(".inventory_list") != ""
        browser.close()


if __name__ == "__main__":
    test_successful_login()