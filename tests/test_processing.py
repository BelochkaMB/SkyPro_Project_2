from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", []),
    ],
)
def test_filter_by_state(sample_transactions: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    result = filter_by_state(sample_transactions, state=state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_default(sample_transactions: List[Dict[str, Any]]) -> None:
    result = filter_by_state(sample_transactions)
    assert [item["id"] for item in result] == [41428829, 939719570]


def test_sort_by_date_descending(sample_transactions: List[Dict[str, Any]]) -> None:
    result = sort_by_date(sample_transactions, reverse=True)
    assert [item["id"] for item in result] == [41428829, 615064591, 594226727, 939719570]


def test_sort_by_date_ascending(sample_transactions: List[Dict[str, Any]]) -> None:
    result = sort_by_date(sample_transactions, reverse=False)
    assert [item["id"] for item in result] == [939719570, 594226727, 615064591, 41428829]


def test_sort_by_date_same_dates(transactions_same_dates: List[Dict[str, Any]]) -> None:
    result = sort_by_date(transactions_same_dates)
    assert [item["id"] for item in result] == [1, 2]


def test_sort_by_date_missing_date(transactions_missing_date: List[Dict[str, Any]]) -> None:
    result = sort_by_date(transactions_missing_date)
    assert [item["id"] for item in result] == [1]
