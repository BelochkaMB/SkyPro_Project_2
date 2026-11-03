from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_account_card: str) -> str | None:
    """
    Функция, маскирует номер счета/карты
    """
    if not mask_account_card.strip():
        return "Ошибка: пустой ввод"

    parts = mask_account_card.split()

    if len(parts) < 2:
        return "Ошибка: некорректный формат данных"

    number = parts[-1]
    name = " ".join(parts[:-1])

    if not number.isdigit():
        return "Ошибка: номер должен состоять только из цифр"

    if name == "Счет":
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Функция, преобразующая строку с датой в формат ДД.ММ.ГГГГ"""

    date_dt = datetime.fromisoformat(date_str)

    return date_dt.strftime("%d.%m.%Y")
