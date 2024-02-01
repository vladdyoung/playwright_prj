""" Страница Alerts, Frame & Windows приложения demoqa """

import allure
from playwright.sync_api import expect

import config
from pages.oscar_sandbox.base_page import BasePage


class WindowPage(BasePage):
    """ Методы для Windows приложения demoqa """

    NEW_TAB_BTN = '#tabButton'
    SAMPLE_HEADING_TXT_NEW_TAB = '#sampleHeading'
    BROWSER_WINDOW = 'Browser Windows'

    def transit_on_new_tab(self):
        self.page.get_by_text(self.BROWSER_WINDOW).click()

        with self.page.context.expect_page() as tab:
            self.page.locator(self.NEW_TAB_BTN).click()

        new_tab = tab.value

        self.should_be_success_transit_on_new_tab(tab_val=new_tab.url,
                                                  new_tab_url=config.NEW_TAB_URL,
                                                  sample_heading_txt=self.SAMPLE_HEADING_TXT_NEW_TAB)

    @allure.step('Проверить успешность перехода на новую страницу')
    def should_be_success_transit_on_new_tab(self, tab_val, new_tab_url, sample_heading_txt):
        with allure.step('Проверить что URL соответствует'):
            assert tab_val == new_tab_url

        with allure.step('Проверить что текст на новой странице виден'):
            expect(self.page.locator(sample_heading_txt))
