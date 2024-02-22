from playwright.sync_api import sync_playwright
from credentials import username, password, SWAG_BASE_URL
from page_actions import login

def test_successful_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        # Выполнение входа с корректными учетными данными
        login(page, SWAG_BASE_URL, username, password)

        # Проверка заголовка страницы после успешного входа
        page_title = page.title()
        assert page_title == "Swag Labs"

        # Проверка наличия продуктов на странице после успешного входа
        assert page.inner_html(".inventory_list") != ""

        # Закрытие браузера
        browser.close()

# Запуск теста
if __name__ == "__main__":
    test_successful_login()