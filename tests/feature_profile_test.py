import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Profile Functionality")
    @allure.severity("CRITICAL")
    @pytest.mark.smoke
    def test_first(self):
        self.loginPage.open()
        self.loginPage.enter_login(self.data.LOGIN)
        self.loginPage.enter_password(self.data.PASSWORD)
        self.loginPage.click_submit_button()
        self.newBiomaterialPage.is_opened()
        self.newBiomaterialPage.click_ordering_button()
        self.analysisOrderingPage.is_opened()
        self.analysisOrderingPage.enter_order_number("7989000776")



