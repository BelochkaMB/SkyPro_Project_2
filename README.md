# SkyPro_Project_2
Проект предназначен для фильтрации, сортировки и потоковой обработки данных о банковских операциях пользователей. Он решает задачу базовой аналитики логов транзакций, помогая отбирать операции по статусу и валюте, упорядочивать их по дате, получать описания транзакций и генерировать номера банковских карт.

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Разработка](#разработка)
- [Тестирование](#тестирование)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- [Python](https://python.org) v3.12+
- [Poetry](https://python-poetry.org) — управление зависимостями
- [Flake8](https://pycqa.org) — линтер кода
- [mypy](https://mypy-lang.org) — статическая типизация
- [pytest](https://docs.pytest.org/en/stable/) — фреймворк для модульного тестирования

## Использование

### Модуль `src.processing`
Для использования функций фильтрации и сортировки импортируйте их из модуля `src.processing`.

#### 1. Фильтрация по статусу (`filter_by_state`)
Функция принимает список словарей и возвращает новый список, содержащий только операции с указанным статусом (по умолчанию `'EXECUTED'`).

```python
from src.processing import filter_by_state

data = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'CANCELED'}
]

# Получить только отмененные операции
canceled_ops = filter_by_state(data, state='CANCELED')
print(canceled_ops)  # Выведет операцию с id: 2
```

#### 2. Сортировка по дате (`sort_by_date`)
Функция сортирует элементы по ключу `date`. По умолчанию сортировка идет по убыванию (от свежих к старым).

```python
from src.processing import sort_by_date

data = [
    {'id': 1, 'date': '2018-06-30T02:08:58.425572'},
    {'id': 2, 'date': '2019-07-03T18:35:29.512364'}
]

# Сортировка от свежих к старым
sorted_ops = sort_by_date(data, reverse=True)
print(sorted_ops)  # Операция с id: 2 будет первой
```

### Модуль `src.generations`
Для потоковой обработки транзакций и генерации номеров карт импортируйте генераторы из модуля `src.generations`.

#### 1. Фильтрация по валюте (`filter_by_currency`)
Функция принимает список словарей с транзакциями и код валюты, возвращая итератор с подходящими операциями.

```python
from src.generations import filter_by_currency

transactions = [
    {
        "id": 939719570,
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
```

#### 2. Генератор описаний транзакций (`transaction_descriptions`)
Генератор принимает список словарей с транзакциями и по очереди возвращает описание каждой операции.

```python
from src.generations import transaction_descriptions

transactions = [
    {"id": 939719570, "description": "Перевод организации"},
    {"id": 142264268, "description": "Перевод со счета на счет"},
]

descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))
```

#### 3. Генератор номеров карт (`card_number_generator`)
Генератор выдает номера банковских карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне (от `0000 0000 0000 0001` до `9999 9999 9999 9999`).

```python
from src.generations import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
```

## Разработка

### Требования
Для работы с проектом необходим установленный Python версии 3.12+ и менеджер пакетов Poetry.

### Установка зависимостей
Для установки всех необходимых библиотек выполните команду:
```sh
poetry install
```

## Тестирование

Проект покрыт модульными тестами с использованием библиотеки `pytest`.

Для запуска тестов и генерации HTML-отчета о покрытии выполните команду:

```bash
pytest --cov=src --cov-report=html
```

Сгенерированный отчет о покрытии сохраняется в директории `htmlcov/` (файл `index.html`).

Для проверки оформления кода и корректности типизации в проекте используются линтеры. Для их запуска выполните команды:

```sh
poetry run flake8 src
poetry run mypy src
```

## To do
- [x] Реализовать функции фильтрации и сортировки (`src.processing`)
- [x] Реализовать генераторы для обработки транзакций и номеров карт (`src.generations`)
- [x] Добавить понятное README по шаблону
- [x] Написать юнит-тесты для модулей (`pytest`)

## Команда проекта
- [Никита / Audi R8](https://github.com) — Python Developer
