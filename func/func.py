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
    """
    :return: Возвращение списка операция
    """
    with open("operations.json", "r", encoding="utf=8") as operation_file:
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
    date_operation = date_operation.split("T")[0]
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
        #   if "date" in operation:
        if operation["date"] == full_date_operation:
            id_operation = operation["id"]  # id
            state_operation = operation["state"]  # Статус
            operation_amount = (operation["operationAmount"])["amount"]  # Сумма перевода
            name_operation = (operation["operationAmount"])["currency"]["name"]  # Валюта
            description_operation = operation["description"]  # описание перевода
            from_operation = operation["from"]
            to_operation = operation["to"]
            return id_operation, state_operation, operation_amount, name_operation, description_operation, from_operation, to_operation


cor = correct_format()


print(f"""{correct_date()} 
{cor[4]} 
{cor[5]} -> 
{cor[6]} 
{cor[2]} 
{cor[3]}""")
"""
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб."""


class Account_transactions:
    """ Класс для показа сообщений об операциях """
    def __init__(self, original_word, valid_word_set):  #      original_word - исходное слово, ,original_word, valid_word_set
        self.original_word = original_word
        self.valid_word_set = valid_word_set
        self.user_response = None


    def __repr__(self):    # не понимаю что сюда нужно прописывать
       return "Класс для проверки ввода слов"


    def word_check(self):   #проверка введеного слова на допустимые слова
        if self.user_response in self.valid_word_set:
            return True
        else:
            return False


    def word_count(self):       #количество допустимых слов
        return len(self.valid_word_set)