from typing import Dict, List


def filter_by_state(list_of_dictionaries: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция, возвращает список словарей у которых ключ state соответствует EXECUTED"""
    filter_operations = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("state") == state:
            filter_operations.append(dictionary)

    return filter_operations


def sort_by_date(list_of_dictionaries: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция принимает на вход список словарей и параметр порядка сортировки.
    Возвращает новый список, отсортированный по дате."""
    filter_list_by_date = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("date") is not None:
            filter_list_by_date.append(dictionary)

    return sorted(filter_list_by_date, key=lambda x: str(x.get("date")), reverse=reverse)
