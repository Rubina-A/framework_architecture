import allure
import requests
from config import settings, test_data


@allure.feature("API Tests")
class TestAPI:

    @allure.story("Получение списка ресторанов")
    def test_get_restaurants(self):
        url = f"{settings.API_URL}/restaurants"
        response = requests.get(url)
        assert response.status_code == 200
        assert "restaurants" in response.json()

    @allure.story("Получение меню ресторана")
    def test_get_menu(self):
        url = f"{settings.API_URL}/restaurants/1/menu"
        response = requests.get(url)
        assert response.status_code == 200
        assert "items" in response.json()

    @allure.story("Добавление товара в корзину")
    def test_add_to_cart(self):
        url = f"{settings.API_URL}/cart/add"
        payload = {"product_id": 101, "quantity": 1}
        response = requests.post(url, json=payload, headers={"Authorization": f"Bearer {test_data.AUTH_TOKEN}"})
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

    @allure.story("Удаление товара из корзины")
    def test_remove_from_cart(self):
        url = f"{settings.API_URL}/cart/remove"
        payload = {"product_id": 101}
        response = requests.post(url, json=payload, headers={"Authorization": f"Bearer {test_data.AUTH_TOKEN}"})
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

    @allure.story("Оформление заказа")
    def test_checkout(self):
        url = f"{settings.API_URL}/checkout"
        payload = {"address": "Новосибирск, Ленина 1", "payment": "card"}
        response = requests.post(url, json=payload, headers={"Authorization": f"Bearer {test_data.AUTH_TOKEN}"})
        assert response.status_code in [200, 400]  # зависит от данных
