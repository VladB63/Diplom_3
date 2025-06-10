import allure
from pages.base_page import BasePage
from locators.personal_page_locators import PersonalPageLoc


class PersonalPage(BasePage):

    @allure.step('Клик по кнопке История заказов')
    def click_to_history_button(self):
        self.click_to_element(PersonalPageLoc.HISTORY_ORDER_BUTTON)


    @allure.step('Клик по кнопке Выход')
    def click_to_exit_button(self):
        self.click_to_element(PersonalPageLoc.EXIT_BUTTON)


    @allure.step('Получение номера заказа из истории')
    def giv_order_number_history(self):
        return self.giv_text_element(PersonalPageLoc.ORDER_NUMBER_HISTORY)


