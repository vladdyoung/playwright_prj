""" Клиент BookStore """


class BookStoreClient:

    def __init__(self, host):
        self._host = host

    # BookStore
    def get_books(self, page):
        """ Получить список всех книг """

        url = f'{self._host}BookStore/v1/Books'
        return page.request.get(url)
