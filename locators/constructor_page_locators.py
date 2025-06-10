from selenium.webdriver.common.by import By

class ConstructorPageLoc:
    LOG_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]' # кнопка войти в аккаунт
    PERSONAL_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]'  # кнопка перехода в личный кабинет
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка оформления заказа
    ORDER_TAPE_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]'  # кнопка перехода на ленту заказов
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]'  # кнопка перехода к конструктору
    INGRIT_BUTTON = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'  # кнопка ингредиента раздела Булки
    MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X pt-10 pb-15'  # модальное окно Детали ингредиента
    CLOSE_MOD_BUTTON = By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]' # кнопка крестик на модальном окне Деталей ингредиента/оформленного заказа
    BURGER_INGRIT = By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_' # блок для переноса ингредиентов
    INGRIT_CLOSE_MODAL = By.XPATH, '(//section[@class="Modal_modal__P3_V5"])[1]' # закрытое модальное окно деталей ингредиента
    COUNT_NUMBER = By.CLASS_NAME, 'counter_counter__num__3nue1' # счетчика каунтера ингредиента
    ORDER_MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal__container__Wo2l_' # модальное окно оформленного заказа
    NEW_NUMBER_ORDER = By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'  # номер только что оформленного заказа

