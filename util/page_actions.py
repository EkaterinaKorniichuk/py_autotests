# page_actions.py

def login(page, SWAG_BASE_URL, username, password):
    page.goto(SWAG_BASE_URL)
    page.fill('input[name="user-name"]', username)
    page.fill('input[name="password"]', password)
    page.click('input[type="submit"]')
    page.wait_for_load_state()


# loginPage = LoginPage()
    # loginPage.go_to()
    #
    # loginPage.username.fill("standard_user")
    # loginPage.password.fill("secret_sauce")
    #
    # loginPage.submit()