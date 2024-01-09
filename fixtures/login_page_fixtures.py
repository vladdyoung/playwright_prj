""" Фикстуры страницы регистрации """

import pytest

from pages.login_page import LoginPage


@pytest.fixture
def del_user_account(page, base_url):
    """ Фикстура удаления аккаунта после прохождения теста с регистрацией нового пользователя в системе """

    yield
    LoginPage(page=page, url=base_url).del_account()
