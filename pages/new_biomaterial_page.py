import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class NewBiomaterialPage(BasePage):

    PAGE_URL = Links.NEW_BIOMATERIAL_PAGE

    ORDERING_BUTTON = ("xpath", "//span[text()='Анализы, БАДы и лекарства']")


    @allure.step("Click on 'Ordering button'")
    def click_ordering_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDERING_BUTTON)).click()