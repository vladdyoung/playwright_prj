""" Базовая страница """
import allure
from playwright.sync_api import Page, expect

from models.session import Session


class BasePage:
    """ Базовая страница. Содержит основные методы для взаимодействия со страницами приложения """

    def __init__(self, page: Page, session: Session, url):
        self.page = page
        self.url = url
        self.session = session

    @allure.step('Открыть браузер')
    def open(self):
        """ Функция открытия страницы приложения и проверки соответствия URL """

        self.page.goto(self.url)  # стандартная фикстура Playwright для старта браузера и открытия URL
        expect(self.page).to_have_url(self.url)  # проверка соответствия URL

    @allure.step('Заполнить поле посимвольно')
    def fill_by_character_field(self, field_name_locator, text):
        field = self.page.locator(field_name_locator)
        field.type(text)  # посимвольное заполнение
        field.press('Enter')

    @allure.step('Заполнить поле')
    def fill_field(self, field_name_locator, text):
        field = self.page.locator(field_name_locator)
        field.fill(text)  # обычное заполнение
        field.press('Enter')
