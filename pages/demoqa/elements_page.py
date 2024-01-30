""" Страница Elements приложения demoqa """

import os
import dotenv
import allure
from playwright.sync_api import expect

from pages.oscar_sandbox.base_page import BasePage


class ElementsPage(BasePage):
    """ Страница Elements приложения demoqa """

    dotenv.load_dotenv()

    ELEMENTS_LIST = 'span:has-text("Elements")'
    EMAIL = os.environ['EMAIL']

    # Text Box
    TEXT_BOX = 'Text Box'
    FULL_NAME = '#userName'
    EMAIL_FIELD = '#userEmail'
    CURRENT_ADDRESS = '#currentAddress'
    PERMANENT_ADDRESS = '#permanentAddress'
    SUBMIT_TEXT_BOX_BTN = '#submit'
    ANSWER_TEXT_BOX = '.border'

    def fell_text_box_form(self, full_name, email, current_address, permanent_ad):
        self.page.get_by_text(self.TEXT_BOX).click()
        self.page.locator(self.FULL_NAME).fill(full_name)
        self.page.locator(self.EMAIL_FIELD).fill(email)
        self.page.locator(self.CURRENT_ADDRESS).fill(current_address)
        self.page.locator(self.PERMANENT_ADDRESS).fill(permanent_ad)
        self.page.locator(self.SUBMIT_TEXT_BOX_BTN).click()

    @allure.step('Проверить успешность работы Text Box')
    def should_be_answer_board(self):
        with allure.step('Проверить что появилось форма ответа'):
            expect(self.page.locator(self.ANSWER_TEXT_BOX)).to_be_visible()




