import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLoc


class OrderFeedPage(BasePage):

    @allure.step('Вызов модального окна с деталями заказа')
    def calling_modal_window_order_details(self):
        self.click_to_element(OrderFeedPageLoc.ORDER_LIST)


    @allure.step('Получение номера заказа в работе')
    def giv_order_number_in_work(self):
        return self.giv_text_element(OrderFeedPageLoc.NUMBER_IN_WORK)


    @allure.step("Получить класс модального окна с деталями заказа")
    def get_class_detail_modal_window(self):
        detail_modal_window = self.giv_class_element(OrderFeedPageLoc.ORDER_DETAIL_MODAL)
        return detail_modal_window


    @allure.step('Получение списка заказов ленты')
    def get_number_list_feed(self):
        numbers = self.find_elements_with_wait(OrderFeedPageLoc.ORDER_NUMBER_IN_FEED)
        order_list = [number.text for number in numbers]
        return order_list

    @allure.step('Получение кол-ва заказов за все время')
    def get_number_orders_all_time(self):
        return self.giv_text_element(OrderFeedPageLoc.ALL_ORDERS_ALL_TIME)


    @allure.step('Получение кол-ва заказов за сегодня')
    def get_number_orders_today(self):
        return self.giv_text_element(OrderFeedPageLoc.ALL_ORDERS_TODAY)

