""" Страница приложения для проверки работы с различными actions """

import allure

from config import TEST_FILES_DIR
from pages.oscar_sandbox.base_page import BasePage


class ActionsPage(BasePage):

    # Alerts
    ALERT = 'Диалог Alert'
    CONFIRM_ALERT = 'Диалог Confirmation'
    PROMPT_ALERT = 'Диалог Prompt'

    # Upload
    UPLOAD_FIELD = '#formFile'
    UPLOAD_BTN = '#file-submit'

    # DragAndDrops
    DRAG = '#drag'
    DROP = '#drop'

    # Alerts methods
    @allure.step('Вызвать Confirm alert')
    def call_confirm_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())  # прослушивает события с диалоговыми окнами (дока)
        self.page.get_by_text(self.CONFIRM_ALERT).click()

    @allure.step('Вызвать Alert')
    def call_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())  # прослушивает события с диалоговыми окнами (дока)
        self.page.get_by_text(self.ALERT).click()

    @allure.step('Вызвать Prompt')
    def call_prompt_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept('30'))  # прослушивает события с диалоговыми окнами (дока)
        self.page.get_by_text(self.PROMPT_ALERT).click()

    # Upload methods
    @allure.step('Загрузить файл первый способ')
    def upload_file_first_method(self, file_name):
        self.page.set_input_files(self.UPLOAD_FIELD, f'{TEST_FILES_DIR}/{file_name}')
        self.page.locator(self.UPLOAD_BTN).click()

    @allure.step('Загрузить файл второй способ с прослушиванием события')
    def upload_file_second_method(self, file_name):
        self.page.on("filechooser", lambda file_chooser: file_chooser.set_files(fr'{TEST_FILES_DIR}/{file_name}'))
        self.page.locator(self.UPLOAD_FIELD).click()
        self.page.locator(self.UPLOAD_BTN).click()

    # DragAndDrop methods
    @allure.step('Перенести файл')
    def drag_and_drop_file(self):
        drag = self.page.query_selector(self.DRAG)
        self.initial_source_position = drag.bounding_box()  # позиция элемента до drag and drop
        self.page.drag_and_drop(self.DRAG, self.DROP)

    @allure.step('Проверить успешность переноса файла')
    def should_be_successful_drag_and_drop(self):
        drag = self.page.query_selector(self.DRAG)
        final_source_position = drag.bounding_box()  # позиция элемента после drag and drop
        with allure.step('Проверить что сработал drag and drop'):
            assert self.initial_source_position['x'] != final_source_position['x']
