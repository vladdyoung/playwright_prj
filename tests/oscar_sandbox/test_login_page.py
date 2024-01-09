import allure
import pytest

from pages.login_page import LoginPage


class TestLoginPage:
    @allure.title('Проверка регистрации нового пользователя')
    @pytest.mark.usefixtures('del_user_account')  # фикстура удаления аккаунта после окончания теста
    def test_reg_new_user(self, page, base_url):
        page = LoginPage(page=page, url=base_url)
        page.open()
        page.go_to_lign_page()
        page.reg_new_user()
        page.should_be_success_registration_new_user()

    @allure.title('Проверка удаления аккаунта')
    def test_del_account(self, page, base_url):
        page = LoginPage(page=page, url=base_url)
        page.open()
        page.go_to_lign_page()
        page.reg_new_user()
        page.should_be_success_registration_new_user()
        page.del_account()
        page.should_be_success_delete_account()



