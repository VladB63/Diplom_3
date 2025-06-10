import allure
from data import UrlPage
from locators.general_lokators import GeneralLoc
from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLoc



class ConstructorPage(BasePage):

    @allure.step('Переход по урлу')
    def open_url_stellar(self):
        self.go_to_url(UrlPage.STELLAR_URL)


    @allure.step('Ожидание когда перестанет отображаться перекрывающий слой')
    def wait_overlaying_element_disappeared(self):
        self.wait_for_invisibility_of_element(GeneralLoc.PROBLEM_MODAL)

    @allure.step('Поиск модального окна оформленного заказа')
    def find_modal_window_in_page(self):
        if self.find_element_with_wait(ConstructorPageLoc.ORDER_MODAL_WINDOW):
            return True
        else:
            return False

    @allure.step("Получить класс закрытого модального окна Деталей ингредиента")
    def get_class_close_modal_window(self):
        close_modal_window = self.giv_class_element(ConstructorPageLoc.INGRIT_CLOSE_MODAL)
        return close_modal_window



    @allure.step('Клик по кнопке Войти в Аккаунт')
    def click_to_log_button(self):
        self.click_to_element(ConstructorPageLoc.LOG_ACCOUNT)


    @allure.step('Клик по кнопке Личный кабинет')
    def click_to_personal_button(self):
        self.click_to_element(ConstructorPageLoc.PERSONAL_ACCOUNT)


    @allure.step('Клик по кнопке Лента заказов')
    def click_to_order_feed(self):
        self.click_to_element(ConstructorPageLoc.ORDER_TAPE_BUTTON)


    @allure.step('Клик по кнопке Конструктор')
    def click_to_constructor_button(self):
        self.click_to_element(ConstructorPageLoc.CONSTRUCTOR_BUTTON)


    @allure.step('Клик по ингредиенту')
    def click_to_ingrit_button(self):
        self.click_to_element(ConstructorPageLoc.INGRIT_BUTTON)


    @allure.step('Получение модального окна Детали ингредиента')
    def giv_modal_window(self):
        return self.find_element_with_wait(ConstructorPageLoc.MODAL_WINDOW).text()


    @allure.step('Закрытие модального окна Детали ингредиента')
    def close_modal_window(self):
        self.find_element_with_wait(ConstructorPageLoc.CLOSE_MOD_BUTTON)
        self.click_to_element(ConstructorPageLoc.CLOSE_MOD_BUTTON)


    @allure.step('Добавление Ингредиента в заказ')
    def drag_and_drop(self):
        elem_from = self.find_element_with_wait(ConstructorPageLoc.INGRIT_BUTTON)
        elem_to = self.find_element_with_wait(ConstructorPageLoc.BURGER_INGRIT)
        self.drag_and_drop_element(elem_from, elem_to)


    @allure.step('Клик по кнопке Оформить заказ')
    def click_to_order_button(self):
        self.click_to_element(ConstructorPageLoc.ORDER_BUTTON)


    @allure.step('Получение значение каунтера ингредиента')
    def giv_number_count(self):
        return self.giv_text_element(ConstructorPageLoc.COUNT_NUMBER)


    @allure.step('Получение номера только что оформленного заказа')
    def giv_new_order_number(self):
        self.wait_for_page_load()
        return f'0{self.giv_text_element(ConstructorPageLoc.NEW_NUMBER_ORDER)}'

