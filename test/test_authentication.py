from playwright.sync_api import sync_playwright
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.credentials import username, password, empty_password, incorrect_username, incorrect_password, empty_username, SWAG_BASE_URL
from util.page_actions import login

def test_login_page_displays_correctly():
 with sync_playwright() as playwright:
    # given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # when
    page.goto(SWAG_BASE_URL)

    # then
    page_title = page.title()
    assert page_title == "Swag Labs"
    login_button = page.wait_for_selector("#login-button")
    assert login_button is not None
    browser.close()

def test_successful_login():
  with sync_playwright() as playwright:
    # given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # when
    login(page, SWAG_BASE_URL, username, password)

    # then
    page_title = page.title()
    assert page_title == "Swag Labs"
    assert page.inner_html(".inventory_list") != ""
    browser.close()

def test_incorrect_username():
  with sync_playwright() as playwright:
    # given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # when
    login(page, SWAG_BASE_URL, incorrect_username, password)

    # then
    error_message = page.text_content('.error-message-container h3')
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    browser.close()

def test_incorrect_password():
 with sync_playwright() as playwright:
    # given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # when
    login(page, SWAG_BASE_URL, username, incorrect_password)

    # then
    error_message = page.text_content('.error-message-container h3')
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    browser.close()

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
    browser.close()

def test_login_failed_when_empty_password():
  with sync_playwright() as playwright:
    # given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # when
    login(page, SWAG_BASE_URL, username, empty_password)

    # then
    error_message = page.text_content('.error-message-container h3')
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
    browser.close()