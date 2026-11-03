def get_mask_card_number(card_number: str) -> str:
    """
    Функция, маскирует номер карты
    """
    card_str = str(card_number)
    if len(card_str) != 16 or not card_number.isdigit():
        return "Некорректная длина номера карты"
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Функция, маскирует номер счета
    """
    account_str = str(account_number)
    if len(account_str) != 20 or not account_number.isdigit():
        return "Некорректная длина номера счета"
    return f"**{account_str[-4:]}"
