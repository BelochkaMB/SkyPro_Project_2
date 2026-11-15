import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Ошибка: пустой ввод"),
        ("   ", "Ошибка: пустой ввод"),
        ("VisaPlatinum", "Ошибка: некорректный формат данных"),
        ("Visa abcd1234", "Ошибка: номер должен состоять только из цифр"),
        ("Visa 12345", "Visa Некорректная длина номера карты"),
        ("Счет 12345", "Счет Некорректная длина номера счета"),
    ],
)
def test_mask_account_card(input_data: str, expected: str) -> None:
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-12-31T23:59:59", "31.12.2020"),
    ],
)
def test_get_date_valid(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected


@pytest.mark.parametrize("invalid_date", ["", "не дата", "2024-99-99"])
def test_get_date_invalid(invalid_date: str) -> None:
    with pytest.raises(ValueError):
        get_date(invalid_date)
