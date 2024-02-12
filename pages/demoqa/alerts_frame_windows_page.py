""" Страница Alerts, Frame & Windows приложения demoqa """

import allure
from playwright.sync_api import expect

import config
from pages.oscar_sandbox.base_page import BasePage


class WindowPage(BasePage):
    """ Методы для работы с Browser Windows приложения demoqa """

    NEW_TAB_BTN = '#tabButton'
    NEW_WIN_BTN = '#windowButton'
    NEW_WIN_MESSAGE_BTN = '#messageWindowButton'
    SAMPLE_HEADING_TXT_NEW_TAB = '#sampleHeading'
    BROWSER_WINDOW = 'Browser Windows'

    def click_browser_window_btn(self):
        self.page.get_by_text(self.BROWSER_WINDOW).click()

    def open_on_new_tab_and_check_success(self):
        self.click_browser_window_btn()

        # Прослушивает событие открытия новой вкладки https://playwright.dev/python/docs/events
        with self.page.context.expect_page() as tab:
            self.page.locator(self.NEW_TAB_BTN).click()

        self.new_tab = tab.value


    def open_new_window(self):
        self.click_browser_window_btn()

        # Прослушивает событие открытия нового окна https://playwright.dev/python/docs/events
        with self.page.expect_event("popup") as page_info:
            self.page.locator(self.NEW_WIN_BTN).click()

        self.popup = page_info.value

    def open_new_window_message(self):
        self.click_browser_window_btn()

        # Прослушивает событие открытия нового окна https://playwright.dev/python/docs/events
        with self.page.expect_event("popup"):
            self.page.locator(self.NEW_WIN_MESSAGE_BTN).click()

    @allure.step('Проверить успешность открытия')
    def should_be_success_open(self, tab_val, new_tab_url, sample_heading_txt):
        with allure.step('Проверить что URL соответствует'):
            assert tab_val == new_tab_url

        with allure.step('Проверить присутствие текста'):
            expect(self.page.locator(sample_heading_txt))

    @allure.step('Проверить наличие текста в новом окне')
    def should_be_exists_text(self, sample_heading_txt):
        with allure.step('Проверить присутствие текста'):
            expect(self.page.locator(sample_heading_txt))
