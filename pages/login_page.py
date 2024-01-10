""" Страница авторизации/регистрации """

import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    """ Страница авторизации/регистрации. Содержит основные методы для взаимодействия со страницей авторизации """

    LOGIN_LINK = '#login_link'
    REG_BTN = '[name="registration_submit"]'
    DEL_BTN = '.btn-danger'
    REG_ADDRESS_FIELD = '#id_registration-email'
    REG_PASS_FIELD = '#id_registration-password1'
    REPEAT_REG_PASS_FIELD = '#id_registration-password2'
    SUCCESS_MESSAGE = '.alertinner.wicon'
    ACCOUNT_LINK = '.icon-user'
    DELETE_PROFILE_BTN = '#delete_profile'
    DEL_PASS_FIELD = '#id_password'

    @allure.step('Перейти на страницу регистрации/авторизации')
    def go_to_lign_page(self):
        self.page.locator(self.LOGIN_LINK).click()

    @allure.step('Зарегистрировать новый аккаунт')
    def reg_new_user(self):
        self.page.locator(self.REG_ADDRESS_FIELD).fill(self.session.auth_data['EMAIL'])
        self.page.locator(self.REG_PASS_FIELD).fill(self.session.auth_data['PASS'])
        self.page.locator(self.REPEAT_REG_PASS_FIELD).fill(self.session.auth_data['PASS'])
        self.page.locator(self.REG_BTN).click()

    @allure.step('Удалить аккаунт')
    def del_account(self):
        self.page.locator(self.ACCOUNT_LINK).click()
        self.page.locator(self.DELETE_PROFILE_BTN).click()
        self.page.locator(self.DEL_PASS_FIELD).fill(self.session.auth_data['PASS'])
        self.page.locator(self.DEL_BTN).click()

    @allure.step('Проверить успешность регистрации нового аккаунта')
    def should_be_success_registration_new_user(self):
        expect(self.page.locator(self.SUCCESS_MESSAGE)).to_have_text(expected='Спасибо за регистрацию!')

    @allure.step('Проверить успешность удаления аккаунта')
    def should_be_success_delete_account(self):
        expect(self.page.locator(self.SUCCESS_MESSAGE)).to_have_text(expected='Ваш профиль удален. Спасибо,'
                                                                              ' что воспользовались нашим сайтом.')
