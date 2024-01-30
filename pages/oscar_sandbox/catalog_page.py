""" Страница каталога приложения """

import allure
from playwright.sync_api import expect

from pages.oscar_sandbox.base_page import BasePage


class CatalogPage(BasePage):

    CATALOG_TITLE = '.page-header'
    LIST_GOODS = 'section .row li'
    COUNT_GOODS_ON_PAGE = '.form-horizontal strong'

    @allure.step('Перейти на страницу товаров с главной страницы')
    def go_to_catalog_page_from_main_page(self):
        self.page.locator(self.SHOW_STORE).click()
        self.page.get_by_text(self.ALL_PRODUCTS).click()  # использовал метод поиска по тексту
        self.should_be_opened_main_catalog()

    @allure.step('Проверка возможности перехода в основной каталог')
    def should_be_opened_main_catalog(self):
        with allure.step('Проверка отображения наименования каталога'):
            expect(self.page.locator(self.CATALOG_TITLE)).to_be_visible()
        with allure.step('Проверка корректности наименования каталога'):
            expect(self.page.locator(self.CATALOG_TITLE)).to_have_text(self.ALL_PRODUCTS)

    @allure.step('Проверка наличия товаров в каталоге')
    def should_be_present_goods_in_catalog(self):
        count_goods = self.page.locator(self.COUNT_GOODS_ON_PAGE).nth(-1).text_content()
        with allure.step('Фактическое количество товаров равно ожидаемому'):
            expect(self.page.locator(self.LIST_GOODS)).to_have_count(int(count_goods))
