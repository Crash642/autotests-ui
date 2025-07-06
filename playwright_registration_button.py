from playwright_registration import LoginPage
from playwright.sync_api import sync_playwright, expect
from tools.routes import AppRoute
from config import settings

def test_button():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=settings.headless)
        page = browser.new_page()
        page.goto(AppRoute.REGISTRATION)
        login_page = LoginPage(page)
        login_button = login_page.login_button
        expect(login_button).to_be_disabled()
        login_page.login('user.name@gmail.com', 'username', 'password', click_login = False)
        expect(login_button).to_be_enabled()
        page.wait_for_timeout(5000)

if __name__ == "__main__":
    test_button()