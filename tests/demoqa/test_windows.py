
import allure
from loguru import logger

from config import DEMOQA_BASE_URL
from pages.demoqa.main_page import MainPage
from pages.demoqa.alerts_frame_windows_page import WindowPage


class TestWindowsPage:
    @logger.catch(reraise=True)
    @allure.title('Проверка работы с новой вкладкой')
    def test_new_tab(self, page, session):
        page = WindowPage(page=page, session=session, url=DEMOQA_BASE_URL)
        page.open()
        page.go_to_page(page_name_locator=MainPage.AL_FR_WIN)
        page.transit_on_new_tab()
