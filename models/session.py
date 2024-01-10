import pytest
from hvac.exceptions import InvalidPath, Forbidden

import config
from helpers import vault_helper


class Session:
    """ Объект, пока содержащий настройки запуска Vault. Далее добавится еще инфа """

    def __init__(self, request):

        # Vault
        self.vault_token = request.config.getoption("--vault_token")

        # Поучить конфигурацию из Vault. Аутентификация по токену.
        # Чтобы получить токен, нужно сначала авторизоваться в Vault под своей учеткой
        vault_secret_path = config.VAULT_SECRET_PATH

        try:
            self.vault_config = vault_helper.get_configuration(secret_path=vault_secret_path, token=self.vault_token,
                                                               url=config.VAULT_URL)
        except (vault_helper.VaultAuthException, InvalidPath, Forbidden) as err:
            pytest.exit(err)

        # email
        self.auth_data = self.vault_config['AUTH_DATA']
