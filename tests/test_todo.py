import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page, base_url) -> None:
    """ Первый тест для понимания playwright

        Args:
            page: стандартная фикстура

        pytest --headed для запуска браузера

    """
    page.goto(base_url)
    page.get_by_role("link", name="List users").click()
    page.locator("li").filter(has_text="List users").click()


def test_demo_playwright(page) -> None:

    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')
    input_fild = page.get_by_placeholder('What needs to be done?')
    expect(input_fild).to_be_empty()
    input_fild.fill('задача номер 1')
    input_fild.press('Enter')
    input_fild.fill('задача номер 2')
    input_fild.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    todo_item.get_by_role('checkbox').nth(0).click()
    expect(todo_item.nth(0)).to_have_class('completed')
    page.pause()
