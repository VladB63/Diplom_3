import allure
from data import PersonData
from pages.base_page import BasePage
from locators.authorization_page_locators import AuthorizationPageLoc



class RecoveryPage(BasePage):

    @allure.step('Клик по кнопке Восстановить пароль')
    def click_to_recover_pass_button(self):
        self.click_to_element(AuthorizationPageLoc.RECOVER_PASS_BUTTON)


    @allure.step('Клик по кнопке Восстановить')
    def click_to_recover_button(self):
        self.click_to_element(AuthorizationPageLoc.RECOVER_BUTTON)


    @allure.step('Ожидание загрузки страницы нового пароля')
    def wait_load_page(self):
        self.wait_for_page_load()
        self.find_element_with_wait(AuthorizationPageLoc.RECOVER_PASS_INPUT)


    @allure.step('Клик по кнопке Показать/Скрыть пароль')
    def click_to_show_hide_button(self):
        self.click_to_element(AuthorizationPageLoc.SHOW_HIDE_BUTTON)
        return AuthorizationPageLoc.ACTIV_FIELD_PASS

    @allure.step('Заполнение поля Email')
    def add_email_type(self):
        self.add_text_to_element(AuthorizationPageLoc.EMAIL_INPUT, PersonData.EMAIL)

