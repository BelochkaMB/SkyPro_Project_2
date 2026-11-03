from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_account_card: str) -> str | None:
    """
    Функция, маскирует номер счета/карты
    """

    parts = mask_account_card.split()

    number = parts[-1]

    name = " ".join(parts[:-1])

    if name == "Счет":
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Функция, преобразующая строку с датой в формат ДД.ММ.ГГГГ"""

    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:10]

    return f"{day}.{month}.{year}"
