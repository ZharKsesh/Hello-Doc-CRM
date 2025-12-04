import allure
import pytest
import os
from dotenv import load_dotenv
from base.base_test import BaseTest
load_dotenv()
@allure.feature("Profile Functionality")
class TestLogin(BaseTest):

    @allure.title("Profile Functionality")
    @allure.severity("CRITICAL")
    @pytest.mark.smoke
    def test_login_with_clinic(self):
        self.loginPage.open()
        self.loginPage.enter_login(os.getenv("LOGIN1_VALID"))
        self.loginPage.enter_password(os.getenv("PASSWORD1_VALID"))
        self.loginPage.click_submit_button()
        self.newBiomaterialPage.is_opened()

    def test_login_without_clinic(self):
        self.loginPage.open()
        self.loginPage.enter_login(os.getenv("LOGIN2_VALID"))
        self.loginPage.enter_password(os.getenv("PASSWORD2_VALID"))
        self.loginPage.click_submit_button()
        self.analysisOrderingPage.is_opened()

    def test_login_invalid(self):
        self.loginPage.open()
        self.loginPage.enter_login(os.getenv("LOGIN3_INVALID"))
        self.loginPage.enter_password(os.getenv("PASSWORD3_INVALID"))
        self.loginPage.click_submit_button()
        banner = self.loginPage.get_invalid_data_banner()
        assert banner is not None
        assert banner.text == "Неверный логин или пароль"




