import allure
from loguru import logger

from config import ALERTS_URL
from pages.actions_page import ActionsPage


class TestAlertPage:
    @logger.catch(reraise=True)
    @allure.title('Проверка взаимодействия с алертами страницы')
    def test_alerts(self, page, session, base_url):
        page = ActionsPage(page=page, session=session, url=ALERTS_URL)
        page.open()
        page.call_alert()
        page.call_confirm_alert()

    @logger.catch(reraise=True)
    @allure.title('Проверка взаимодействия с prompt алертом страницы')
    def test_prompt_alert(self, page, session, base_url):
        page = ActionsPage(page=page, session=session, url=ALERTS_URL)
        page.open()
        page.call_prompt_alert()
