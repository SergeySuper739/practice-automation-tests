# UI-автотесты Practice Automation

Проект UI-автотестов для https://practice-automation.com/ на Python + Selenium + Pytest + Allure.

## Стек
- Python 3.12+
- Selenium 4
- Pytest
- Allure
- webdriver-manager

## Установка
pip install -r requirements.txt

## Запуск
pytest
allure serve allure-results

## Структура
- pages/ — Page Object Model
- tests/ — тесты
- conftest.py — фикстуры + скриншоты при падении

## Тест-кейсы

### Календарь (позитив 4 + негатив 2)
- Открытие календаря
- Выбор даты
- Следующий месяц
- Предыдущий месяц
- Невалидная дата
- Текст вместо даты

### Модальные окна (позитив 4 + негатив 1)
- Открытие Simple Modal
- Закрытие Simple Modal
- Открытие Form Modal
- Заполнение формы
- Пустая форма

### Рекламные окна (позитив 2 + негатив 1)
- Открытие страницы
- Закрытие рекламы
- Проверка URL

### Форма Automation Tools
- Заполнение Message списком
- Пустое Message
