
import allure
from loguru import logger

import config
from config import DEMOQA_BASE_URL
from data.api_data.book_store_api_data import EXISTS_TEXT_NEW_WINDOW_MESSAGE
from pages.demoqa.main_page import MainPage
from pages.demoqa.alerts_frame_windows_page import WindowPage


class TestWindowsPage:
    @logger.catch(reraise=True)
    @allure.title('Работа с новой вкладкой')
    def test_new_tab(self, page, session):
        page = WindowPage(page=page, session=session, url=DEMOQA_BASE_URL)
        page.open()
        page.go_to_page(page_name_locator=MainPage.AL_FR_WIN)
        page.open_on_new_tab_and_check_success()

    @logger.catch(reraise=True)
    @allure.title('Работа с новым окном')
    def test_new_tab(self, page, session):
        page = WindowPage(page=page, session=session, url=DEMOQA_BASE_URL)
        page.open()
        page.go_to_page(page_name_locator=MainPage.AL_FR_WIN)
        page.open_new_window()
        page.should_be_success_open(tab_val=page.popup.url,
                                    new_tab_url=config.NEW_TAB_URL,
                                    sample_heading_txt=page.SAMPLE_HEADING_TXT_NEW_TAB)

    @logger.catch(reraise=True)
    @allure.title('Работа с новым текстовым окном')
    def test_new_tab(self, page, session):
        page = WindowPage(page=page, session=session, url=DEMOQA_BASE_URL)
        page.open()
        page.go_to_page(page_name_locator=MainPage.AL_FR_WIN)
        page.open_new_window_message()
        page.should_be_exists_text(sample_heading_txt=EXISTS_TEXT_NEW_WINDOW_MESSAGE)
