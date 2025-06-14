from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
import allure


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_registration_input = Input(page,'registration-form-email-input', 'registration_Email')
        self.username_registration_input = Input(page,'registration-form-username-input', 'registration_Username')
        self.password_registration_input = Input(page,'registration-form-password-input', 'registration_Password')

    @allure.step("Fill registration form")
    def fill(self, email: str, username:str, password: str):
        self.email_registration_input.fill(email)
        self.username_registration_input.fill(username)
        self.password_registration_input.fill(password)

    @allure.step("Check visible registration form")
    def check_visible(self, email: str, username: str, password: str):
        self.email_registration_input.check_visible()
        self.username_registration_input.check_visible()
        self.password_registration_input.check_visible()

        self.email_registration_input.check_have_value(email)
        self.username_registration_input.check_have_value(username)
        self.password_registration_input.check_have_value(password)