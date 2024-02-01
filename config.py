""" Основной конфиг проекта """

import os

# Базовые страницы для приложений
OSCAR_SANDBOX_BASE_URL = 'https://selenium1py.pythonanywhere.com/ru/'
ACTIONS_BASE_URL = 'https://zimaev.github.io/'
DEMOQA_BASE_URL = 'https://demoqa.com/'

# Конфиг для oscar_sandbox
CATALOGUE_URL = f'{OSCAR_SANDBOX_BASE_URL}catalogue/'
LOGIN_URL = f'{OSCAR_SANDBOX_BASE_URL}accounts/login/'

ALERTS_URL = f'{ACTIONS_BASE_URL}dialog/'
UPLOAD_FILES_URL = f'{ACTIONS_BASE_URL}upload/'
DRAG_AND_DROP_URL = f'{ACTIONS_BASE_URL}draganddrop/'

# Конфиг для demoqa
NEW_TAB_URL = f'{DEMOQA_BASE_URL}sample'

# Конфиг для локального Vault
VAULT_URL = 'http://127.0.0.1:8200'
VAULT_SECRET_PATH = 'oscar_sandbox'

# Path
ROOT_DIR = os.path.dirname(__file__)
TEST_FILES_DIR = os.path.join(ROOT_DIR, 'data')
