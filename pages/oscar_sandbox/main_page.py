""" Главная страница приложения """

import allure
from playwright.sync_api import expect

from pages.oscar_sandbox.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Сменить язык')
    def change_language(self):  # впадающий список
        self.page.select_option(self.LANGUAGE_LIST, 'en-gb')
        self.page.locator(self.SUBMIT_BTN).click()

    @allure.step('Заполнить поле поиска посимвольно')
    def fill_search_field_by_character(self, text):
        self.fill_by_character_field(field_name_locator=self.SEARCH_PRODUCT_FIELD, text=text)

    @allure.step('Проверить смену языка')
    def should_be_changed_language(self):
        response = self.page.request.get(self.page.url)
        content_length = response.headers['content-language']

        with allure.step('Проверка смены языка'):
            assert content_length == 'en-gb'

        expect(self.page.locator(self.SUBMIT_BTN)).to_have_text(expected='Go')

    @allure.step('Проверить работоспособность поискового поля')
    def should_be_work_search_fill(self):
        expect(self.page.locator(self.PRODUCT)).to_be_visible()
