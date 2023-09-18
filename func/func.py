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
    """ Функция для получение 5 последних операций """
    json_operation = load_operation_json()
    date_operation = []
    for operation in json_operation:
        if "date" in operation:
            date_operation.append(operation["date"])
    date_operation.sort()
    return list(reversed(date_operation[-5:]))



