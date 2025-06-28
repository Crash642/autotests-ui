from time import sleep

from playwright.sync_api import sync_playwright
from tools.routes import AppRoute

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(AppRoute.LOGIN)

    # Устанавливаем фокус на поле Email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in 'user@gmail.com':
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.press(character, delay=300)

    # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    page.keyboard.press("ControlOrMeta+A")
    
    # Ждём 5 секунд для наглядности результата
    page.wait_for_timeout(5000)

    # type() – если нужно просто ввести текст в поле ввода, делает это более высокоуровнево.
    # keyboard.press() – если нужно эмулировать реальные нажатия клавиш, например, Enter, Tab, Backspace, или вводить текст в нестандартных элементах.