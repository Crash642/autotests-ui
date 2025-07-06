from playwright.sync_api import sync_playwright
from tools.routes import AppRoute
from config import settings

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(AppRoute.LOGIN)
    
    # Находим ссылку Registration
    registration_link = page.get_by_test_id('login-page-registration-link')
    # Выполняем наведение курсора на ссылку
    registration_link.hover()

    # Добавляем паузу для наглядности результата
    page.wait_for_timeout(5000)

# mouse.move(x, y) — перемещение курсора в указанные координаты.
# mouse.click(x, y) — клик в определённой точке экрана.
# mouse.down() и mouse.up() — для работы с зажатием и отпусканием кнопки мыши.