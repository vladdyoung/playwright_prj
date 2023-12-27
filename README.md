# python_playwright
## Semple work with Python Playwright librery

### Установка:
```commandline
pip install playwright
pip install pytest-playwright
playwright install // все браузеры
playwright install firefox // только firefox
```

Запуск скрипта:
```commandline
playwright codegen my_url
```

Дополнительные опции codegen доступны по команде 
```commandline
playwright codegen --help
```

Сохранить код в файл:
```commandline
playwright codegen -o main.py https://playwright-todomvc.antonzimaiev.repl.co
```

Для запуска браузера
```commandline
pytest --headed для запуска браузера
```

### Список проверок
```commandline
expect(locator).to_be_checked()	Checkbox  установлен
expect(locator).to_be_disabled()	Веб-элемент отключен
expect(locator).to_be_editable()	Веб-элемент возможно редактировать 
expect(locator).to_be_empty()	Веб-элемент пустой
expect(locator).to_be_enabled()	Веб-элемент включен/активен
expect(locator).to_be_focused()	Веб-элемент находится в фокусе
expect(locator).to_be_hidden()	Веб-элемент не отображается
expect(locator).to_be_visible()	Веб-элемент видим/отображается
expect(locator).to_contain_text()	Веб-элемент содержит текст(текст передается аргументом к проверке)
expect(locator).to_have_attribute()	Веб-элемент имеет атрибут(атрибут передается аргументом к проверке)
expect(locator).to_have_class()	Элемент имеет класс (класс передается аргументом к проверке)
expect(locator).to_have_count()	Список имеет указанное количество/длину
expect(locator).to_have_css()	Элемент имеет CSS свойство (свойство передается аргументом к проверке)
expect(locator).to_have_id()	Элемент имеет идентификатор (идентификатор передается аргументом к проверке)
expect(locator).to_have_js_property()	Элемент имеет JavaScript свойство (свойство передается аргументом к проверке)
expect(locator).to_have_text()	Элемент имеет текст (проверяемый текст передается аргументом к проверке)
expect(locator).to_have_value()	Input имеет значение (проверяемое значение передается аргументом к проверке)
expect(locator).to_have_values()	Select имеет опции для выбора (опция передается аргументом к проверке)
expect(page).to_have_title()	Страница имеет  title (текст  title передается аргументом к проверке)
expect(page).to_have_url()	Страница имеет URL (URL передается аргументом к проверке)
expect(api_response).to_be_ok()	Ответ имеет статус OK
```


### PWDEBUG и Playwright Inspector
```commandline
можно засунуть в CLI, можно в Environment при запуске из PyCharm
PWDEBUG=1  открыть инструмент для дебагинга

Chrome DevTools
playwright.$(selector): выделяет первое вхождение селектора.
playwright.$$(селектор): выделяет все вхождения селектора. 
playwright.inspect(selector):  переместит во вкладу элементы и отобразит данный селектор в DOM
playwright.generateLocator($0):  сгенерировать локатор
```

### Логирование API Playwright
```commandline
DEBUG=pw:api
```

### Trace Viewer
```commandline
Запись трассировки
pytest --tracing
='on'- Запишет трассировку для каждого теста. (не рекомендуется, так как производительность тяжелая)
='retain-on-failure'- Запишет трассировку для каждого теста, но удалит ее из успешных тестовых прогонов.

Просмотр трассировки
playwright show-trace trace.zip

page.pause()  пауза для теста
page.wait_for_timeout(3000)  таймаут для теста на 30 сек
```

### Путь до pytest_addoptions в pytest_playwight
```commandline
jetbrains://pycharm/navigate/reference?project=python_playwright&path=~\AppData\Local\Programs\Python\Python310\Lib\site-packages\pytest_playwright\pytest_playwright.py
```

### Только браузер firefox
```commandline
в pytest.ini указать несколько браузеров: --browser chromium --browser firefox
в тесте использовать фикстуру: @pytest.mark.only_browser("firefox")
могут быть неожиданные результаты работы!
```