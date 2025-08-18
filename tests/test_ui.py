import allure
import pytest
from pages.main_page import MainPage
from config import settings


@allure.feature("UI Tests")
class TestUI:

    @allure.story("Поиск товара")
    def test_search_product(self, driver):
        page = MainPage(driver, settings.BASE_URL)
        page.open()
        page.search_product("молоко")
        assert "молоко" in driver.page_source

    @allure.story("Открытие страницы ресторана")
    def test_open_restaurant_page(self, driver):
        page = MainPage(driver, settings.BASE_URL)
        page.open()
        first_restaurant = page.find(("css selector", "a[href*='/restaurant']"))
        first_restaurant.click()
        assert "restaurant" in driver.current_url

    @allure.story("Добавление товара в корзину")
    def test_add_to_cart(self, driver):
        page = MainPage(driver, settings.BASE_URL)
        page.open()
        product = page.find(("css selector", "button[data-auto='addToCartButton']"))
        product.click()
        cart = page.find(("css selector", "a[href*='/cart']"))
        cart.click()
        assert "Корзина" in driver.page_source

    @allure.story("Удаление товара из корзины")
    def test_remove_from_cart(self, driver):
        page = MainPage(driver, settings.BASE_URL)
        page.open()
        product = page.find(("css selector", "button[data-auto='addToCartButton']"))
        product.click()
        cart = page.find(("css selector", "a[href*='/cart']"))
        cart.click()
        remove_btn = page.find(("css selector", "button[data-auto='removeFromCartButton']"))
        remove_btn.click()
        assert "Корзина пуста" in driver.page_source

    @allure.story("Фильтрация по категории")
    def test_filter_category(self, driver):
        page = MainPage(driver, settings.BASE_URL)
        page.open()
        category = page.find(("css selector", "a[href*='category']"))
        category.click()
        assert "category" in driver.current_url
