import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath","//input[@id='login-input']")
    PASSWORD_FIELD = ("xpath","//input[@id='password-input']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    INVALID_DATA_BANNER = ("xpath", "//div[@role='alert']")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click on 'Submit button'")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def get_invalid_data_banner(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.INVALID_DATA_BANNER)
        )
