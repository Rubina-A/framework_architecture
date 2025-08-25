from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder*='Поиск']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def search_product(self, query: str):
        self.find(self.SEARCH_FIELD).send_keys(query)
        self.click(self.SEARCH_BUTTON)
