import pytest
from playwright.sync_api import expect, Page
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic 
from tools.allure.features import AllureFeature 
from tools.allure.stories import AllureStory 
from allure_commons.types import Severity
from tools.routes import AppRoute
from config import settings




@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS) 
@allure.feature(AllureFeature.AUTHENTICATION) 
@allure.story(AllureStory.REGISTRATION) 
@allure.parent_suite(AllureEpic.LMS) 
@allure.suite(AllureFeature.AUTHENTICATION) 
@allure.sub_suite(AllureStory.REGISTRATION) 

class TestRegistration:
    @pytest.mark.xdist_group(name="authorization-group")
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage,dashboard_page: DashboardPage):  
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
        email = settings.test_user.email,
        username = settings.test_user.username, 
        password = settings.test_user.password
        )
        
        registration_page.registration_form.check_visible(
            email = settings.test_user.email,
            username = settings.test_user.username, 
            password = settings.test_user.password
        )

        registration_page.click_registration_button()
        dashboard_page.toolbar.check_visible()
