


def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    ''' Функция, возвращает список словарей у которых ключ state соответствует EXECUTED '''
    filter_operations = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("state") == state:
            filter_operations.append(dictionary)

    return filter_operations


def sort_by_date(list_of_dictionaries: list[dict], reverse: bool = True) -> list[dict]:
    """ Функция принимает на вход список словарей и параметр порядка сортировки.
       Возвращает новый список, отсортированный по дате. """
    filter_list_by_date = []
    for dictionary in list_of_dictionaries:
        if dictionary.get("date") is not None:
            filter_list_by_date.append(dictionary)

    return sorted(filter_list_by_date, key=lambda x: x["date"], reverse=reverse)



if __name__ == "__main__":
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    print("--- Проверка фильтрации (только CANCELED) ---")
    print(filter_by_state(data, "CANCELED"))

    print("\n--- Проверка сортировки по дате (от свежих к старым) ---")
    print(sort_by_date(data, reverse=True))