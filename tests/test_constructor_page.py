import allure
from data import PersonData, UrlPage, ModalWindow
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage


class TestConstructorPage:

    @allure.title('Проверка перехода кнопки Конструктор')
    def test_constructor_button(self, driver):
        cp = ConstructorPage(driver)
        cp.open_url_stellar()
        cp.click_to_personal_button()
        cp.click_to_constructor_button()
        current_url = cp.get_current_url()
        assert current_url == UrlPage.STELLAR_URL


    @allure.title('Проверка открытия модального окна Деталей ингредиентов')
    def test_open_modal_window_ingrit(self, driver):
        cp = ConstructorPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_ingrit_button()
        current_url = cp.get_current_url()
        assert UrlPage.INGRIT_URL in current_url

    @allure.title('Проверка закрытия модального окна Деталей ингредиентов')
    def test_close_modal_window_ingrit(self, driver):
        cp = ConstructorPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_ingrit_button()
        cp.close_modal_window()
        assert cp.get_class_close_modal_window() == ModalWindow.MODAL_WINDOW_CLOSE

    @allure.title('Проверка счетчика ингредиента при добавлении')
    def test_change_counter_ingrid(self, driver):
        cp = ConstructorPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.drag_and_drop()
        assert cp.giv_number_count() == PersonData.NUMBER_COUNT


    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_making_order_with_login(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        cp.drag_and_drop()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_order_button()
        assert cp.find_modal_window_in_page()
