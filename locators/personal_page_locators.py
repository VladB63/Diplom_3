from selenium.webdriver.common.by import By


class PersonalPageLoc:
    HISTORY_ORDER_BUTTON = By.XPATH, '//a[@href="/account/order-history"]'  # кнопка история заказов в лк
    ORDER_NUMBER_HISTORY = By.XPATH, '(//p[@class="text text_type_digits-default"])[1]'  # первый номер заказа из истории заказов
    EXIT_BUTTON = By.XPATH, './/button[text()="Выход"]'  # кнопка выхода из лк