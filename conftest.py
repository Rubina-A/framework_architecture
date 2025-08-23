import pytest
from selenium import webdriver


@pytest.fixture
def open_base():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://market-delivery.yandex.ru")
    yield driver
    driver.quit()
