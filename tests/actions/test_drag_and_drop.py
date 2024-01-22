import allure
from loguru import logger

from config import DRAG_AND_DROP_URL
from pages.actions_page import ActionsPage


class TestDragAndDropPage:
    @logger.catch(reraise=True)
    @allure.title('Проверка работы drag and drop')
    def test_drag_and_drop(self, page, session, base_url):
        page = ActionsPage(page=page, session=session, url=DRAG_AND_DROP_URL)
        page.open()
        page.drag_and_drop_file()
        page.should_be_successful_drag_and_drop()
