from playwright.sync_api import sync_playwright, expect
from tools.routes import AppRoute
from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)
    
    login_button = page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    context.storage_state(path = settings.browser_state_file)



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state = settings.browser_state_file) # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto(AppRoute.COURSES)
    
    courses_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text('Courses')
   
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    courses_text_result = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_text_result).to_be_visible()
    expect(courses_text_result).to_have_text('There is no results')

    courses_text_displayed = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_text_displayed).to_be_visible()
    expect(courses_text_displayed).to_have_text('Results from the load test pipeline will be displayed here')
    page.wait_for_timeout(5000)