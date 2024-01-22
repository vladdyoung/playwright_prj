import allure
from loguru import logger

from config import CATALOGUE_URL
from pages.catalog_page import CatalogPage


class TestCatalogPage:
    @logger.catch(reraise=True)
    @allure.title('Проверка наличия товаров в основном каталоге')
    def test_present_goods_in_catalog(self, page, session, base_url):
        page = CatalogPage(page=page, session=session, url=CATALOGUE_URL)
        page.open()
        page.should_be_opened_main_catalog()
        page.should_be_present_goods_in_catalog()
