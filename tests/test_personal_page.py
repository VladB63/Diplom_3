import allure
from data import UrlPage
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.personal_page import PersonalPage


class TestPersonalPage:

    @allure.title('Проверка перехода в личный кабинет')
    def test_click_button_personal_page(self, driver):
        cp = ConstructorPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        current_url = cp.get_current_url()
        assert current_url == UrlPage.AUTH_URL

    @allure.title('Проверка просмотра истории заказов')
    def test_history_order(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        pp = PersonalPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_personal_button()
        pp.click_to_history_button()
        cp.wait_for_page_load()
        current_url = pp.get_current_url()
        assert current_url == UrlPage.HISTORY_URL


    @allure.title('Проверка кнопки Выход')
    def test_exit_button(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        pp = PersonalPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_personal_button()
        pp.click_to_exit_button()
        ap.find_log_button()
        current_url = pp.get_current_url()
        assert current_url == UrlPage.AUTH_URL
