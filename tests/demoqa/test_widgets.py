import allure
from loguru import logger

from config import DEMOQA_BASE_URL
from pages.demoqa.main_page import MainPage
from pages.demoqa.widgets import WidgetsPage


class TestWidgetsPage:
    @logger.catch(reraise=True)
    @allure.title('Проверка наличия нескольких объектов в форме "Type multiple color names"')
    def test_type_multiple_color_names(self, page, session, base_url):
        page = WidgetsPage(page=page, session=session, url=DEMOQA_BASE_URL)
        page.open()
        page.go_to_page(page_name_locator=MainPage.WIDGETS)
        page.go_to_tab(text=page.AUTO_COMPLETE)
        page.multiple_fill_form()
        page.should_be_match_number_element_in_form(element=page.ADD_MULTIPLE_COLOR_NAME, count_elements=2)

    @logger.catch(reraise=True)
    @allure.title('Проверка наличия объекта в форме "Type single color name"')
    def test_type_single_color_name(self, page, session, base_url):
        page = WidgetsPage(page=page, session=session, url=DEMOQA_BASE_URL)
        page.open()
        page.go_to_page(page_name_locator=MainPage.WIDGETS)
        page.go_to_tab(text=page.AUTO_COMPLETE)
        page.single_fill_form()
        page.should_be_one_element_in_form()
