import pytest
from loguru import logger

from config import BASE_URL
from models.session import Session

# регистрация фикстур
pytest_plugins = (
    'fixtures.login_page_fixtures'
)


def pytest_addoption(parser):
    """ Функция добавления параметров в командную строку перед запуском тестов
        (pytest-хук для регистрации параметров)

    """

    parser.addoption(
        "--url",
        default=BASE_URL,
        help="Enter url"
    )
    parser.addoption(
        "--vault_token",
        action="store",
        help='Токен для доступа к vault')


@pytest.fixture(scope='session')
def base_url(request):
    """ Базовый URL

        return: возвращает либо стандарный url, либо тот, который передан в командную строку
    """

    return request.config.getoption('--url')


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """ Фикстура для редактирования параметров (контекста) браузера

        Desc:
            Словарь со значениями, которые изменяют тот или иной параметр браузера

        return: словарь с измененными значениями браузера
    """

    con = {**browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
    return con


@pytest.fixture(scope="session", autouse=True)
def logger_prj():
    """ Фикстура для логирования с помощью LOGURU"""

    logger.add('../../logs/log.log', format='{time} {level} {message}', level='ERROR', rotation='100 KB',
               compression='zip')


@pytest.fixture(scope='session', autouse=True)
def session(request):
    """ Фикстура для инициализации Session

    Args:
        request: Объект, передаваемый от pytest. Нужен для анализа контекста

    Returns:
        s: Инициализированный Session
    """
    s = Session(request=request)
    yield s
