# framework_architecture
Дипломная работа. Архитектура фреймворка


# Структура проекта
FRAMEWORK ARCHITECTURE/
├── config/ # Конфигурационные файлы
│ ├── settings.py # Настройки окружения
│ └── test_data.py # Тестовые данные
├── pages/ # Page Object Model
│ ├── base_page.py # Базовый класс страницы
│ └── main_page.py # Главная страница и её элементы
├── tests/ # Тестовые наборы
│ ├── test_api.py # API тесты
│ └── test_tui.py # UI тесты
├── conftest.py # Фикстуры Pytest
├── pytest.ini # Конфигурация Pytest
├── requirements.txt # Зависимости Python
└── README.md # Документация 

text

# Используемые библиотеки

Основные зависимости проекта указаны в `requirements.txt`:

- **pytest**: Фреймворк для написания и запуска тестов
- **selenium**: Автоматизация браузера для UI-тестов
- **requests**: Выполнение HTTP-запросов для API-тестов
- **allure-pytest**: Генерация красивых отчетов о тестировании
- **webdriver-manager**: Управление драйверами браузеров

# Установка и настройка

1. Клонируйте репозиторий 
2. Установите зависимости
   pip install -r requirements.txt
Настройте конфигурацию в config/settings.py:

API_URL: Базовый URL для API-запросов

Другие параметры окружения

# Запуск тестов

- Запуск всех тестов
pytest

- Запуск только UI-тестов
pytest tests/test_tui.py -v

- Запуск только API-тестов
pytest tests/test_api.py -v