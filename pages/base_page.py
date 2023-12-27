""" Базовая страница """
import allure
from playwright.sync_api import Page, expect


class BasePage:
    """ Базовая страница. Содержит основные методы для взаимодействия со страницами приложения """

    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    @allure.step('Открыть браузер')
    def open(self):
        """ Функция открытия страницы приложения и проверки соответствия URL """

        self.page.goto(self.url)  # стандартная фикстура Playwright для старта браузера и открытия URL
        expect(self.page).to_have_url(self.url)  # проверка соответствия URL


