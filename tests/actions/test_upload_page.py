import allure
import pytest
from loguru import logger

from config import UPLOAD_FILES_URL
from pages.actions_page import ActionsPage


class TestUploadPage:
    @logger.catch(reraise=True)
    @allure.title('Проверка загрузки файла (первый способ)')
    @pytest.mark.parametrize('file_name', ['sampleFile.jpeg'])
    def test_upload_file_first_method(self, page, session, base_url, file_name):
        page = ActionsPage(page=page, session=session, url=UPLOAD_FILES_URL)
        page.open()
        page.upload_file_first_method(file_name=file_name)

    @logger.catch(reraise=True)
    @allure.title('Проверка загрузки файла (второй способ - прослушивание события)')
    @pytest.mark.parametrize('file_name', ['sampleFile.jpeg'])
    def test_upload_file_second_method(self, page, session, base_url, file_name):
        page = ActionsPage(page=page, session=session, url=UPLOAD_FILES_URL)
        page.open()
        page.upload_file_second_method(file_name=file_name)
