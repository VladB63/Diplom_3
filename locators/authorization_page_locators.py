from selenium.webdriver.common.by import By


class AuthorizationPageLoc:
    LOG_ACCOUNT = By.XPATH, './/button[text()="Войти в аккаунт"]'  # кнопка войти в аккаунт на главной странице
    AUTH_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка войти в аккаунт после ввода кредов
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input[@name="name"]'  # поле Email
    PASS_INPUT = By.XPATH, './/label[text()="Пароль"]/following-sibling::input[@name="Пароль"]'  # поле пароль
    RECOVER_PASS_BUTTON = By.XPATH, './/a[@href="/forgot-password"]' # кнопка Восстановить пароль страницы авторизации
    RECOVER_BUTTON = By.XPATH, './/button[text()="Восстановить"]'  # кнопка Восстановить
    RECOVER_PASS_INPUT = By.XPATH, './/label[text()="Пароль"]'  # поле пароль страницы восстановления пароля
    SHOW_HIDE_BUTTON = By.CLASS_NAME, 'input__icon.input__icon-action' # кнопка/показать скрыть пароль
    ACTIV_FIELD_PASS = By.XPATH, './/input[type()="text"]' # состояние активного поля для ввода пароля

