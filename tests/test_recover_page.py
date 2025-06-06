import allure
from data import UrlPage
from pages.constructor_page import ConstructorPage
from pages.pass_recovery_page import RecoveryPage


class TestRecoverPage:

    @allure.title('Проверка перехода на страницу Восстановление пароля')
    def test_recovery_pass(self, driver):
        cp = ConstructorPage(driver)
        rp = RecoveryPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        rp.click_to_recover_pass_button()
        current_url = rp.get_current_url()
        assert current_url == UrlPage.RECOVER_PASS_URL


    @allure.title('Проверка ввода почты и клик кнопки Восстановить')
    def test_add_email_and_click_button(self, driver):
        cp = ConstructorPage(driver)
        rp = RecoveryPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        rp.click_to_recover_pass_button()
        rp.add_email_type()
        rp.click_to_recover_button()
        rp.wait_load_page()
        current_url = rp.get_current_url()
        assert current_url == UrlPage.RESET_PASS_URL

    @allure.title('Проверка фокуса поля Пароль')
    def test_focus_field(self, driver):
        cp = ConstructorPage(driver)
        rp = RecoveryPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        rp.click_to_recover_pass_button()
        rp.add_email_type()
        rp.click_to_recover_button()
        cp.wait_overlaying_element_disappeared()
        rp.click_to_show_hide_button()
        assert rp.click_to_show_hide_button()
