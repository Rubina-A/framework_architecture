import allure
import requests
from config import settings, test_data


@allure.feature("API Tests — Поиск")
class TestAPISearch:

    endpoint = f"{settings.API_URL}/eats/v1/full-text-search/v1/search"

    headers = {
        "Content-Type": "application/json"
    }

    cookies = test_data.COOKIES   # вынесли куки в отдельный файл

    @allure.story("Поиск по названию на кириллице")
    def test_search_cyrillic(self):
        payload = {
            "text": "магнит косметик",
            "filters": [],
            "location": {"longitude": 82.88865760667233, "latitude": 55.01369962898733}
        }
        response = requests.post(self.endpoint, json=payload, headers=self.headers, cookies=self.cookies)
        assert response.status_code == 200

    @allure.story("Поиск по названию на латинице")
    def test_search_latin(self):
        payload = {
            "text": "apple",
            "filters": [],
            "location": {"longitude": 82.88865760667233, "latitude": 55.01369962898733}
        }
        response = requests.post(self.endpoint, json=payload, headers=self.headers, cookies=self.cookies)
        assert response.status_code == 200

    @allure.story("Поиск по названию с цифрами")
    def test_search_digits(self):
        payload = {
            "text": "13",
            "filters": [],
            "location": {"longitude": 82.88865760667233, "latitude": 55.01369962898733}
        }
        response = requests.post(self.endpoint, json=payload, headers=self.headers, cookies=self.cookies)
        assert response.status_code == 200

    @allure.story("Пустой поиск")
    def test_search_empty(self):
        payload = {
            "text": "",
            "filters": [],
            "location": {"longitude": 82.88865760667233, "latitude": 55.01369962898733}
        }
        response = requests.post(self.endpoint, json=payload, headers=self.headers, cookies=self.cookies)
        assert response.status_code == 200

    @allure.story("Поиск по произвольному набору символов")
    def test_search_symbols(self):
        payload = {
            "text": "!@#$%",
            "filters": [],
            "location": {"longitude": 82.88865760667233, "latitude": 55.01369962898733}
        }
        response = requests.post(self.endpoint, json=payload, headers=self.headers, cookies=self.cookies)
        assert response.status_code == 200
