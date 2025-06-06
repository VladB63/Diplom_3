from selenium.webdriver.common.by import By


class GeneralLoc:

    PROBLEM_MODAL = By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]' # перекрывающее окно