from playwright.sync_api import sync_playwright
from tools.routes import AppRoute
from config import settings

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(
        AppRoute.LOGIN,
        wait_until='networkidle'  # Ждем полной загрузки страницы
    )

    # Выполняем JS-код для замены текста заголовка
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

    # Добавляем паузу для наглядности
    page.wait_for_timeout(5000)

    