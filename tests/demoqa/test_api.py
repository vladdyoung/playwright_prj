import allure
from loguru import logger


class TestBookStore:
    @logger.catch(reraise=True)
    @allure.title('Проверка наличия всех книг в каталоге')
    def test_get_books(self, page, session):
        books = session.books_store.get_books(page=page)
        with allure.step('Проверка, что каталог не пустой'):
            assert len(books.json()) != 0
