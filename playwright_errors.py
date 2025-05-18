from playwright.sync_api import sync_playwright, expect

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Пытаемся проверить, что несуществующий локатор виден на странице
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Пытаемся ввести текст в кнопку Login
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')
    
    # Пытаемся изменить текст заголовка
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

# Ожидание завершилось с ошибкой:
    
# AssertionError: Locator expected to be visible: скрипт ожидал, что локатор будет виден, но он не найден.
    
# waiting for get_by_test_id("login-page-login-button"): playwright нашел локатор кнопки.

# Locator resolved to <button>...: элемент успешно найден, но его свойства (например, disabled) не позволяют выполнить действие.

# element is not enabled: playwright ожидал, что элемент станет активным и доступным для взаимодействия, но этого не произошло.

# TypeError: Cannot set properties of null: элемент не найден, так как не успел загрузиться.