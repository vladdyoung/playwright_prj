import allure
import pytest
from loguru import logger

from pages.login_page import LoginPage


class TestLoginPage:
    @logger.catch(reraise=True)
    @allure.title('Проверка регистрации нового пользователя')
    @pytest.mark.usefixtures('del_user_account')  # фикстура удаления аккаунта после окончания теста
    def test_reg_new_user(self, page, session, base_url):
        page = LoginPage(page=page, session=session, url=base_url)
        page.open()
        page.go_to_lign_page()
        page.reg_new_user()
        page.should_be_success_registration_new_user()

    @logger.catch(reraise=True)
    @allure.title('Проверка удаления аккаунта')
    def test_del_account(self, page, session, base_url):
        page = LoginPage(page=page, session=session, url=base_url)
        page.open()
        page.go_to_lign_page()
        page.reg_new_user()
        page.should_be_success_registration_new_user()
        page.del_account()
        page.should_be_success_delete_account()



