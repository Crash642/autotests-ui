from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
import allure


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', 'Create course title')
        self.create_course_button = Button(page,'create-course-toolbar-create-course-button', 'Create course button')

    @allure.step("Check visible create course toolbar")
    def check_visible(self, is_create_course_disabled=True):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_visible()


    def click_create_course_button(self):
        self.create_course_button.click()

