import pytest

from src.generations import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> list[dict]:
    """Фикстура с тестовым списком транзакций в разных валютах."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод с карты на карту",
            "from": "Карта 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


@pytest.mark.parametrize(
    ("currency", "expected_ids"),
    [
        ("USD", [939719570, 142264268]),
        ("RUB", [873106923]),
        ("EUR", []),
    ],
)
def test_filter_by_currency(sample_transactions: list[dict], currency: str, expected_ids: list[int]) -> None:
    """Проверяет фильтрацию транзакций по заданной валюте и отсутствие нужной валюты."""
    result = list(filter_by_currency(sample_transactions, currency))
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_currency_empty() -> None:
    """Проверяет, что генератор не падает с ошибкой на пустом списке."""
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    """Проверяет генерацию описаний для списка транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty() -> None:
    """Проверяет работу генератора описаний на пустом списке."""
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    ("start", "stop", "expected"),
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
        (5, 5, ["0000 0000 0000 0005"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    """Проверяет диапазон, форматирование и крайние значения генератора карт."""
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_stop_iteration() -> None:
    """Проверяет корректное завершение генерации (StopIteration)."""
    gen = card_number_generator(1, 1)
    assert next(gen) == "0000 0000 0000 0001"
    with pytest.raises(StopIteration):
        next(gen)
