class HomePage:
    def __init__(self, page):
        self.page = page

    def verify_page_title(self, expected_title):
        actual_title = self.page.title()
        assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

    def verify_all_products_displayed(self):
        assert self.page.inner_html(".inventory_list") != "", "No products are displayed"