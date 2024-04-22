import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        print("Launching browser...")
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        yield browser
        print("Closing browser...")
        browser.close()

