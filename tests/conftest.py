import pytest
from selenium import webdriver


browser_name = None

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param

    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()


