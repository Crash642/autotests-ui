from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    
    courses_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text('Courses')

    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    courses_text_result = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_text_result).to_be_visible()
    expect(courses_text_result).to_have_text('There is no results')

    courses_text_displayed = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_text_displayed).to_be_visible()
    expect(courses_text_displayed).to_have_text('Results from the load test pipeline will be displayed here')


