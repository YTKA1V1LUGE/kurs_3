"""
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
"""
import json
import datetime
"""
import requests
import json
import random
from basic_word import BasicWord


def load_random_word():
    Функция получения слов
    req = requests.get('https://www.jsonkeeper.com/b/A9AI')
    data = json.loads(req.text)
     загрузка списка слов

    random.shuffle(data)  #перемешивание списка

    basic_word = []
    for values in data:
        original_word = values["word"]
        valid_word_set = values["subwords"]
        basic = BasicWord(original_word, valid_word_set)
        basic_word.append(basic)
    return basic_word"""


def load_operation_json():
    """Функция получение слов"""
    with open("operations.json", "r", encoding = "utf=8") as operation_file:
        return json.load(operation_file)


def sort_operation():
    """
    Сортировка и получение последних 5 операция
    :return: Последние 5 операция
    """
    json_operation = load_operation_json()
    date_operation = []
    for operation in json_operation:
        if "date" in operation:
            date_operation.append(operation["date"])
    date_operation.sort()
    return list(reversed(date_operation[-5:]))


def correct_date():
    """
    Функция для возврата даты
    :return: корректный формат даты
    """
    full_date_operation = (sort_operation()[1])
    date_operation = "".join(full_date_operation)
    date_operation = date_operation .split("T")[0]
    date_operation = date_operation.split("-")
    year = date_operation[0]
    month = date_operation[1]
    days = date_operation[2]
    date = f"{days}.{month}.{year}"
    return date, full_date_operation


"""
def correct_date():
    " Скорее более лаконичное использование, но если нужны именно точки то верхняя функция "
    date_operation = (sort_operation()[1])
    date_operation = "".join(date_operation)
    date_operation = date_operation .split("T")[0]
    #date_operation = datetime.datetime.strptime(date_operation, '%Y-%m-%d').date()
    return date_operation
"""


def correct_format():
    json_operation = load_operation_json()
    full_date_operation = correct_date()[1]
    for operation in json_operation:
        if "date" in operation:
            if operation["date"] == full_date_operation:
                id_operation = operation["id"]
                state_operation = operation["state"]
                adjacent_meaning = operation["operationAmount"]      #не помню как словарь в словаре
                amount_operation = adjacent_meaning["amount"]
                adjacent = adjacent_meaning["currency"]
                print(adjacent["name"])

"""
- `state` — статус перевода:
    - `EXECUTED`  — выполнена,
    - `CANCELED`  — отменена.
- `operationAmount` — сумма операции и валюта
- `description` — описание типа перевода
- `from` — откуда (может отсутстовать)
- `to` — куда"""


print(correct_format())