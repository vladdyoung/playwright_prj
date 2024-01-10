import allure
from loguru import logger

from pages.main_page import MainPage


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
    def test_search_field(self, page, session, base_url):
        page = MainPage(page=page, session=session, url=base_url)
        page.open()
        page.fill_search_field_by_character()
        page.should_be_work_search_fill()
