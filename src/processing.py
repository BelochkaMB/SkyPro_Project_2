from typing import Any, Dict, List


def filter_by_state(list_of_dictionaries: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает список словарей, у которых ключ state соответствует EXECUTED"""
    filter_operations = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("state") == state:
            filter_operations.append(dictionary)

    return filter_operations


def sort_by_date(list_of_dictionaries: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает на вход список словарей и параметр порядка сортировки.
    Возвращает новый список, отсортированный по дате.
    """
    filter_list_by_date = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("date") is not None:
            filter_list_by_date.append(dictionary)

    # Исправлена ошибка в lambda: убрана лишняя аннотация типа прямо внутри выражения
    return sorted(filter_list_by_date, key=lambda x: str(x.get("date", "")), reverse=reverse)
