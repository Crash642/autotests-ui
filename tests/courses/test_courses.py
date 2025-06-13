from playwright.sync_api import expect, Page
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import pytest
import re
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic 
from tools.allure.features import AllureFeature 
from tools.allure.stories import AllureStory 
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES) 
@allure.story(AllureStory.COURSES) 
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES) 
@allure.sub_suite(AllureStory.COURSES) 
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar.check_visible()
        courses_list_page.check_visible_empty_view()
        
    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        create_course_page.create_course_exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.toolbar.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
    
    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        create_course_page.create_course_toolbar.click_create_course_button()
        create_course_page.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.toolbar.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        courses_list_page.course_view_menu.click_edit(index=0)
        create_course_page.create_course_form_component.fill(
            title="Playwright updated",
            estimated_time="5 weeks",
            description="Playwright updated",
            max_score="500",
            min_score="9"
        )
        create_course_page.create_course_toolbar.click_create_course_button()
        create_course_page.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.toolbar.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright updated",
            max_score="500",
            min_score="9",
            estimated_time="5 weeks"
        )
