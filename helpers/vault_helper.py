""" Вспомогательные функции для работы с Vault """

import re
from typing import Dict, Union

import hvac

# from data.static_data.workplace import DEFAULT_DOMAIN
# from models.workplace_user import WorkplaceUser


class VaultAuthException(Exception):
    """ Ошибка аутентификации в Vault """
    pass


def get_configuration(secret_path: str, token: str, url: str) -> Dict[str, Union[str, Dict]]:
    """ Получение конфигурации из Vault

    Args:
        secret_path: Путь к секрету в Vault
        token: Токен авторизации
        url: Адрес Vault

    Returns:
        result: Конфигурация Vault
    """
    client = hvac.Client(url=url, verify=False, token=token)
    if not client.is_authenticated():
        raise VaultAuthException('Ошибка аутентификации в Vault')
    secret_version_response = client.secrets.kv.v2.read_secret_version(path=secret_path)
    secret_data = secret_version_response['data']['data']
    result = {k: parse_config_string(v) for k, v in secret_data.items()}
    return result


def parse_config_string(config_string: Union[str, Dict]):
    """ Преобразование строки, содержащей сложную конфигурацию, в словарь
        Пример строки: email=example; password=example
        Пример преобразованной строки:
        {
            'email': 'example',
            'password': 'example'
        }

    Args:
        config_string: строка с конфигурацией

    Returns:
        parsed: Преобразованная в словарь строка с конфигурацией
    """
    parts = tuple(p.strip().split('=') for p in config_string.split(';') if p)
    if len(parts) == 1 and len(parts[0]) == 1:
        parsed = parts[0][0]
    else:
        parsed = {p[0]: p[1] for p in parts}
    return parsed


# def parse_user(role: str, user: str) -> WorkplaceUser:
#     r""" Получение данных пользователя в виде экземпляра WorkplaceUser из строк формата:
#         domain\username@password
#         username@password
#
#     Args:
#         role: Роль пользователя. Аттрибут WorkplaceRoles
#         user: строка с данными пользователя
#
#     Returns:
#         result: экземпляр WorkplaceUser
#     """
#     domain = DEFAULT_DOMAIN
#     if re.match(r'^.*\\.*@.*$', user):
#         username, password = user.split('@')
#         domain, username = username.split('\\')
#     elif re.match(r'^.*@.*$', user):
#         username, password = user.split('@')
#     else:
#         raise ValueError(f'Некорректный формат строки с информацией о пользователе: {user}')
#     result = WorkplaceUser(role=role, username=username, password=password, domain=domain)
#     return result
