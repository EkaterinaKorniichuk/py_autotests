from playwright.sync_api import sync_playwright
from credentials import username, password, SWAG_BASE_URL
from page_actions import login

   # when
def test_login_successful():
  with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    #def test_login_successful(): позволяет pytest автоматически обнаруживать
    #и выполнять эту функцию в качестве теста при запуске тестового процесса.
    #Плюс у нас есть from page_actions import login выше

    login(page, SWAG_BASE_URL, username, password)

    # then
    page_title = page.title()
    assert page_title == "Swag Labs"
    print("Products page loaded successfully.")
    browser.close()


    #assert используется для проверки того, что заголовок страницы (полученный с помощью page.title()) соответствует ожидаемому значению "Swag Labs".
    #Если условие page_title == "Swag Labs" истинно,
    # то программа продолжает выполнение без изменений,
    # и выводится сообщение "Products page loaded successfully.".
    # Если условие ложно, assert генерирует исключение AssertionError,
    # которое может быть обработано далее в программе.
    # Это помогает убедиться, что страница загрузилась правильно и содержит ожидаемый заголовок.


    # loginPage = LoginPage()
    # loginPage.go_to()
    #
    # loginPage.username.fill("standard_user")
    # loginPage.password.fill("secret_sauce")
    #
    # loginPage.submit()