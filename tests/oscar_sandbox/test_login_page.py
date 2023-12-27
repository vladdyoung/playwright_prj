import allure
import pytest

from pages.login_page import LoginPage


@allure.suite('Test Registration Page')
class TestLoginPage:
    @allure.title('Test registration new user')
    @pytest.mark.usefixtures('del_user_account')
    def test_reg_new_user(self, page, base_url):
        page = LoginPage(page=page, url=base_url)
        page.open()
        page.go_to_lign_page()
        page.reg_new_user()
        page.should_be_success_registration_new_user()

    @allure.title('Test delete account')
    def test_del_account(self, page, base_url):
        page = LoginPage(page=page, url=base_url)
        page.open()
        page.go_to_lign_page()
        page.reg_new_user()
        page.should_be_success_registration_new_user()
        page.del_account()
        page.should_be_success_delete_account()



