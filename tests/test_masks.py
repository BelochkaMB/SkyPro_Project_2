import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("12345", "Некорректная длина номера карты"),
        ("12345678901234567890", "Некорректная длина номера карты"),
        ("abcd567812345678", "Некорректная длина номера карты"),
        ("", "Некорректная длина номера карты"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("12345", "Некорректная длина номера счета"),
        ("12345678901234567890123", "Некорректная длина номера счета"),
        ("abcd5678901234567890", "Некорректная длина номера счета"),
        ("", "Некорректная длина номера счета"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
