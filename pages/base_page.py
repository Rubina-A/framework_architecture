from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    def open(self, path: str = "") -> None:
        """Открыть страницу"""
        self.driver.get(self.base_url + path)

    def find(self, locator: tuple, timeout: int = 10):
        """Найти элемент"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple) -> None:
        """Кликнуть по элементу"""
        self.find(locator).click()
