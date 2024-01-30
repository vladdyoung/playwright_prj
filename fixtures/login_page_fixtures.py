""" Фикстуры страницы регистрации """

import pytest

from pages.oscar_sandbox.login_page import LoginPage


@pytest.fixture
def del_user_account(page, session, base_url):
    """ Фикстура удаления аккаунта после прохождения теста с регистрацией нового пользователя в системе """

    yield
    LoginPage(page=page, session=session, url=base_url).del_account()
