from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(mask_account_card: str) -> str | None:
    """Функция, маскирует номер счета/карты"""

    parts = mask_account_card.split()

    number = parts[-1]

    name = " ".join(parts[:-1])

    if name == "Счет":
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"
