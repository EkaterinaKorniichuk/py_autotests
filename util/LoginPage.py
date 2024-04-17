class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto_login_page(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill('input[name="user-name"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('input[type="submit"]')
        self.page.wait_for_load_state()