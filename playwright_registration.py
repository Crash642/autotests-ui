from playwright.sync_api import sync_playwright, expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('registration-page-registration-button')
   
    def login(self,email_input, username, password):
        self.email_input.fill(email_input)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

def test_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        login_page = LoginPage(page)
        login_page.login('user.name@gmail.com', 'username', 'password')
        dashboard_text = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_text).to_be_visible()
        page.wait_for_timeout(5000)


test_registration()