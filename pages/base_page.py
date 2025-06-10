import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Переход по урлу')
    def go_to_url(self, url):
        self.driver.get(url)


    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)


    @allure.step('Ожидание закрытия модалки')
    def wait_for_invisibility_of_element(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))


    @allure.step('Клик по элементу с ожиданием')
    def click_to_element(self, locator):
        self.wait_for_page_load()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    @allure.step('Ввод текста в поле')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение ссылки')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Ожидание загрузки страницы')
    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')


    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)


    @allure.step('Получить текст элемента')
    def giv_text_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Получение класса элемента")
    def giv_class_element(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute("class")