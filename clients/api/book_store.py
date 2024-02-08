""" Клиент для books_store """


class BookStoreAPIClient:

    def __init__(self, host):
        self._host = host

    def get_books(self, page):
        """ Получить список всех книг """

        url = f'{self._host}BookStore/v1/Books'
        return page.request.get(url)
