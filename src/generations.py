from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Возвращает итератор с транзакциями, где валюта операции соответствует заданной."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой транзакции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
