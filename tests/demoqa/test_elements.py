
import allure
import pytest
from loguru import logger

from config import DEMOQA_BASE_URL
from pages.demoqa.elements_page import ElementsPage
from pages.demoqa.main_page import MainPage


class TestElementsPage:
    @logger.catch(reraise=True)
    @allure.title('')
    @pytest.mark.parametrize('full_name, email, current_address, permanent_ad', [
        pytest.param(
            'TestName',
            ElementsPage.EMAIL,
            'TestCurrentAddress',
            'TestPermAd'
        )
    ])
    def test_text_box(self, page, session, base_url, full_name, email, current_address, permanent_ad):
        page = ElementsPage(page=page, session=session, url=DEMOQA_BASE_URL)
        page.open()
        page.go_to_page(page_name_locator=MainPage.ELEMENTS)
        page.fell_text_box_form(full_name=full_name, email=email, current_address=current_address,
                                permanent_ad=permanent_ad)
        page.should_be_answer_board()


