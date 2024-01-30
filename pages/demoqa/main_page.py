""" Главная страница приложения demoqa """

from pages.oscar_sandbox.base_page import BasePage


class MainPage(BasePage):
    ELEMENTS = 'h5:has-text("Elements")'


