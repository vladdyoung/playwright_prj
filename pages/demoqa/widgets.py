""" Страница Widgets приложения demoqa """


import allure
from playwright.sync_api import expect

from pages.oscar_sandbox.base_page import BasePage


class WidgetsPage(BasePage):
    """ Страница Widgets приложения demoqa """

    WIDGETS_BTN = 'span:has-text("Widgets")'
    AUTO_COMPLETE = 'Auto Complete'
    MULTIPLE_CONTAINER_INPUT = '#autoCompleteMultipleContainer input'
    SINGLE_COLOR_NAME_INPUT = '#autoCompleteSingle input'
    SINGLE_COLOR_NAME = '.auto-complete__single-value'
    COLOR_LINK = '#react-select-2-option-0'
    WHITE_LINK = '#react-select-3-option-0'
    ADD_MULTIPLE_COLOR_NAME = '.css-1rhbuit-multiValue'

    def multiple_fill_form(self):
        self.fill_by_character_field(field_name_locator=self.MULTIPLE_CONTAINER_INPUT, text='Green')
        self.page.locator(self.COLOR_LINK).click()

        self.fill_by_character_field(field_name_locator=self.MULTIPLE_CONTAINER_INPUT, text='Red')
        self.page.locator(self.COLOR_LINK).click()

    def single_fill_form(self):
        self.fill_by_character_field(field_name_locator=self.SINGLE_COLOR_NAME_INPUT, text='White')
        self.page.locator(self.WHITE_LINK).click()

    def should_be_match_number_element_in_form(self, element, count_elements):
        with allure.step('Проверить количество добавленных элементов в форме'):
            expect(self.page.locator(element)).to_have_count(count_elements)

    def should_be_one_element_in_form(self):
        with allure.step('Проверить наличие текста в форме'):
            expect(self.page.locator(self.SINGLE_COLOR_NAME)).to_have_text('White')
