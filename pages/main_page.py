""" Главная страница приложения """

import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class MainPage(BasePage):

    LANGUAGE_LIST = '#language_selector .form-control'
    SUBMIT_BTN = '#language_selector .btn-default'
    SEARCH_PRODUCT_FIELD = '#id_q'
    PRODUCT = '.product_pod'

    @allure.step('Сменить язык')
    def change_language(self):
        self.page.select_option(self.LANGUAGE_LIST, 'en-gb')
        self.page.locator(self.SUBMIT_BTN).click()

    @allure.step('Заполнить поле поиска посимвольно')
    def fill_search_field_by_character(self):
        self.fill_by_character_field(field_name_locator=self.SEARCH_PRODUCT_FIELD, text="The shellcoder's handbook")

    @allure.step('Проверить смену языка')
    def should_be_changed_language(self):
        response = self.page.request.get(self.page.url)
        content_length = response.headers['content-language']

        assert content_length == 'en-gb'

        expect(self.page.locator(self.SUBMIT_BTN)).to_have_text(expected='Go')

    @allure.step('Проверить работоспособность поискового поля')
    def should_be_work_search_fill(self):
        expect(self.page.locator(self.PRODUCT)).to_be_visible()
