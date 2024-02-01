import allure
import pytest
from loguru import logger

from pages.oscar_sandbox.main_page import MainPage


class TestMainPage:

    @logger.catch(reraise=True)
    @allure.title('Проверка смены языка')
    def test_change_language(self, page, session, base_url):
        page = MainPage(page=page, session=session, url=base_url)
        page.open()
        page.change_language()
        page.should_be_changed_language()

    @logger.catch(reraise=True)
    @allure.title('Проверка работы поля поиска продукта')
    @pytest.mark.parametrize('text', ["The shellcoder's handbook"])
    def test_search_field(self, page, session, base_url, text):
        page = MainPage(page=page, session=session, url=base_url)
        page.open()
        page.fill_search_field_by_character(text=text)
        page.should_be_work_search_fill()
