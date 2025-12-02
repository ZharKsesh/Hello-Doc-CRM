import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AnalysisOrderingPage(BasePage):

    PAGE_URL = Links.ANALYSIS_ORDERING_PAGE

    SEARCH_FILD = ("xpath", "//input[@placeholder='Поиск по номеру заказа, ФИО и телефону']")

    @allure.step("Enter order number")
    def enter_order_number(self, order_number):
        search_fild = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FILD))
        search_fild.clear()
        assert search_fild.get_attribute("value") == "", "Тут что-то есть"
        search_fild.send_keys(order_number)
