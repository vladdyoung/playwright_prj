from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)  # запуск браузера chromium
    context = browser.new_context()  # создает изолированный сеанс браузера
    page = context.new_page()  # открывает новую страницу(tab) в браузере
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Hello World!!!")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
