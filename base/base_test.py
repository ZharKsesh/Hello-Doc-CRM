import pytest
import os
from config.data import Data
from pages.login_page import LoginPage
from pages.analysis_ordering_page import AnalysisOrderingPage
from pages.new_biomaterial_page import NewBiomaterialPage


class BaseTest:

    data: Data
    loginPage: LoginPage
    analysisOrderingPage: AnalysisOrderingPage
    newBiomaterialPage: NewBiomaterialPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.loginPage = LoginPage(driver)
        request.cls.analysisOrderingPage = AnalysisOrderingPage(driver)
        request.cls.newBiomaterialPage = NewBiomaterialPage(driver)