import pytest
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


@allure.feature("UI Tests — Поиск и корзина")
class TestUI:

    @allure.story("Поиск ресторана Бургер Кинг")
    def test_search_burger_king(self, open_base: WebDriver):
        driver = open_base

        with allure.step("Находим поле поиска и вводим 'Бургер Кинг'"):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='Найти ресторан, блюдо или товар']")
                )
            )
            search_input.clear()
            search_input.send_keys("Бургер Кинг")

        with allure.step("Нажимаем кнопку 'Найти'"):
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[span[text()='Найти']]")
                )
            )
            search_button.click()

        with allure.step("Ждем появления результата поиска и кликаем на ресторан"):
            burger_king_link = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@data-testid='place-header-root']//span[text()='Бургер Кинг']/ancestor::a")
                )
            )
            burger_king_link.click()

        with allure.step("Проверяем, что страница ресторана открыта"):
            restaurant_title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[text()='Бургер Кинг']")
                )
            )
            assert restaurant_title.is_displayed(), "Страница ресторана не открылась"

    @allure.story("Поиск ресторана 'Вкусно и точка' и проверка отсутствия")
    def test_search_vkusno_i_tochka(self, open_base: WebDriver):
        driver = open_base

        with allure.step("Вводим в поиск 'Вкусно и точка'"):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='Найти ресторан, блюдо или товар']")
                )
            )
            search_input.send_keys("Вкусно и точка")

        with allure.step("Нажимаем кнопку 'Найти'"):
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Найти']]"))
            )
            search_button.click()

        with allure.step("Проверяем, что среди найденных ресторанов нет 'Вкусно и точка'"):
            results_loaded = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='place-header-root']"))
            )
            restaurants = driver.find_elements(By.CSS_SELECTOR, "span.r1vfw7r0.p12jp99q.tyhfsqm.beptjsx.b9iv4kk.t1db1e91")
            restaurant_names = [r.text for r in restaurants]
            assert "Вкусно и точка" not in restaurant_names

    @allure.story("Поиск несуществующего ресторана 'Весло'")
    def test_search_nonexistent_restaurant(self, open_base: WebDriver):
        driver = open_base

        with allure.step("Вводим в поиск 'Весло'"):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='Найти ресторан, блюдо или товар']")
                )
            )
            search_input.send_keys("Весло")

        with allure.step("Нажимаем кнопку 'Найти'"):
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Найти']]"))
            )
            search_button.click()

        with allure.step("Проверяем, что ресторана 'Весло' нет среди найденных"):
            restaurants = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='place-header-root']")
            restaurant_names = [r.text for r in restaurants]
            assert "Весло" not in restaurant_names

    @allure.story("Добавление одного бургера в корзину")
    def test_add_burger_to_cart(self, open_base: WebDriver):
        driver = open_base

        with allure.step("Поиск ресторана 'Бургер Кинг' и переход на его страницу"):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='Найти ресторан, блюдо или товар']")
                )
            )
            search_input.clear()
            search_input.send_keys("Бургер Кинг")

            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Найти']]"))
            )
            search_button.click()

            burger_king_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@data-testid='place-header-root']//span[text()='Бургер Кинг']/ancestor::a")
                )
            )
            burger_king_link.click()

            windows = driver.window_handles
            driver.switch_to.window(windows[-1])

            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

        with allure.step("Выбор первого бургера 'Воппер' и добавление в корзину"):
            first_menu_item = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//li[contains(@name,'menu-item-container')][1]//button[contains(@aria-label,'Воппер')]")
                )
            )
            first_menu_item.click()

            modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.o16qwsa7"))
            )

            first_option = WebDriverWait(modal, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ool04b8"))
            )
            first_option.click()

            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.pwwswtx > button"))
            )
            add_button.click()
                        
            next_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.r1jyb6b1"))
            )
            assert next_button is not None, "Кнопка 'Далее' не найдена"

    @allure.story("Добавление 10 бургеров Воппер в корзину")
    def test_add_10_burgers_to_cart(self, open_base: WebDriver):
        driver = open_base

        with allure.step("Поиск ресторана 'Бургер Кинг' и переход на его страницу"):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='Найти ресторан, блюдо или товар']")
                )
            )
            search_input.clear()
            search_input.send_keys("Бургер Кинг")

            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Найти']]"))
            )
            search_button.click()

            burger_king_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@data-testid='place-header-root']//span[text()='Бургер Кинг']/ancestor::a")
                )
            )
            burger_king_link.click()

            windows = driver.window_handles
            driver.switch_to.window(windows[-1])

            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

        with allure.step("Выбор первого бургера 'Воппер' и первой опции"):
            first_menu_item = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//li[contains(@name,'menu-item-container')][1]//button[contains(@aria-label,'Воппер')]")
                )
            )
            first_menu_item.click()

            modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.o16qwsa7"))
            )

            first_option = WebDriverWait(modal, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ool04b8"))
            )
            first_option.click()

        with allure.step("Увеличение количества бургеров до 10"):
            increase_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Увеличить']"))
            )
            for _ in range(9):
                increase_button.click()
                time.sleep(0.2)

        with allure.step("Нажатие кнопки 'Добавить' для добавления 10 бургеров в корзину"):
            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.pwwswtx > button"))
            )
            add_button.click()

            next_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.r1jyb6b1"))
            )
            assert next_button is not None, "Кнопка 'Далее' не найдена"