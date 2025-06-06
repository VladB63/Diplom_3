import allure
from data import PersonData
from pages.base_page import BasePage
from locators.authorization_page_locators import AuthorizationPageLoc


class AuthPage(BasePage):

    @allure.step('Заполнение полей емейл/пароль при авторизации и клик кнопки войти')
    def add_auth_field_click(self):
        self.add_text_to_element(AuthorizationPageLoc.EMAIL_INPUT, PersonData.EMAIL)
        self.add_text_to_element(AuthorizationPageLoc.PASS_INPUT, PersonData.PASSWORD)
        self.click_to_element(AuthorizationPageLoc.AUTH_BUTTON)


    @allure.step('Поиск кнопки войти')
    def find_log_button(self):
        self.find_element_with_wait(AuthorizationPageLoc.AUTH_BUTTON)
