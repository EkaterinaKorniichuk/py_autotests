# page_actions.py

def login(page, SWAG_BASE_URL, username, password):
    page.goto(SWAG_BASE_URL)
    page.fill('input[name="user-name"]', username)
    page.fill('input[name="password"]', password)
    page.click('input[type="submit"]')
    page.wait_for_load_state()
