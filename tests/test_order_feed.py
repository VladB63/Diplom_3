import allure
from locators.order_feed_page_locators import OrderFeedPageLoc
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_page import PersonalPage


class TestOrderFeed:

    @allure.title('Проверка окна с деталями по заказу')
    def test_modal_window_order_details(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_order_feed()
        op = OrderFeedPage(driver)
        op.calling_modal_window_order_details()
        assert OrderFeedPageLoc.ORDER_DETAIL_MODAL


    @allure.title('Проверка отображения заказа из Истории в Ленте')
    def test_displaying_order_history_in_feed(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        pp = PersonalPage(driver)
        op = OrderFeedPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_personal_button()
        pp.click_to_history_button()
        number_list = op.get_number_list_feed()
        assert pp.giv_order_number_history() in number_list


    @allure.title('Проверка счётчика Выполнено за всё время')
    def test_counter_order_all_in_all_time(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        op = OrderFeedPage(driver)
        cp.wait_overlaying_element_disappeared()
        cp.click_to_order_feed()
        amount = op.get_number_orders_all_time()
        cp.click_to_constructor_button()
        cp.drag_and_drop()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_order_button()
        cp.wait_overlaying_element_disappeared()
        cp.close_modal_window()
        cp.click_to_order_feed()
        assert int(amount) + 1


    @allure.title('Проверка счётчика Выполнено за сегодня')
    def test_counter_order_all_in_all_time(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        op = OrderFeedPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_order_feed()
        amount = op.get_number_orders_today()
        cp.click_to_constructor_button()
        cp.drag_and_drop()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_order_button()
        cp.wait_overlaying_element_disappeared()
        cp.close_modal_window()
        cp.click_to_order_feed()
        assert int(amount) + 1


    @allure.title('Проверка номера заказа в работе')
    def test_counter_order_all_in_all_time(self, driver):
        cp = ConstructorPage(driver)
        ap = AuthPage(driver)
        op = OrderFeedPage(driver)
        cp.open_url_stellar()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_log_button()
        ap.add_auth_field_click()
        cp.drag_and_drop()
        cp.wait_overlaying_element_disappeared()
        cp.click_to_order_button()
        cp.wait_overlaying_element_disappeared()
        new_order = cp.giv_new_order_number()
        cp.close_modal_window()
        cp.click_to_order_feed()
        order_in_work = op.giv_order_number_in_work()
        assert new_order == order_in_work
