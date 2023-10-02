import json
from datetime import datetime
import os


def load_operation_json():
    utils_path = os.path.dirname(__file__)
    operation_path = os.path.join(utils_path, "operations.json")
    with open(operation_path, "r", encoding="utf=8") as operation_file:
        return json.load(operation_file)


def filter_by_status(load_operation_lists):
    """
    :param load_operation_lists: общий список операций
    :return: список операций которые выполнены
    """
    filter_by = []  # список выполненых операций
    load_operation = load_operation_lists

    for operation in load_operation:
        if "state" in operation:
            if operation["state"] == "EXECUTED":
                filter_by.append(operation)

    return filter_by


"""Я не понимаю логику как прописать sort operation, если выводить по одному
и если использовать датайм то по идеи нужно брать точку отчета от которой идут даты, а мы можем ее не знать
или сравнивать даты, но если так делать то я придумал лишь использовать метод сортировки по типу пузыря, 
но тогда кода станет только больше"""


def sort_operation(load_operation):
    """
    :param load_operation: список операция
    :return: Список из последних 5 операций
    """
    load = load_operation
    date_operation = []  # список для дат всех операций
    operation_list = []  # список для 5 операций

    for operation in range(len(load)):
        if "date" in load[operation]:
            date_operation.append(load[operation]["date"])  # добавляем даты в список

    date_operation.sort()
    full_date_operation = list(reversed(date_operation[-5:]))  # получаем последние 5 операций

    for date in full_date_operation:
        for operation in load:
            if date in operation["date"]:
                operation_list.append(operation)

    return operation_list


def correct_format_date(original_date):
    """
    :param original_date:  Получаем дату по типу 2022-01-01T12:00:00.000000
    :return: Возвращаем дату по типу 01.01.2022
    """
    datetime_obj = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S.%f")
    correct_date = datetime_obj.strftime("%d.%m.%Y")

    return correct_date


def from_card_hide(sender_number):
    """
    :param sender_number: Получчаем значение карты по типу Visa Classic 1234567890123456
    :return: Возвращаем Visa Classic 1234 56** **** 3456
    """
    sender_number = sender_number
    string = ""  # строка для объеденения списка цифр
    number_list = sender_number.split()  # преобразование входной строки в список
    number = number_list.pop(-1)  # забираем именно цифры

    number = number[:-(len(number) - 6)] + '*' * (
            len(number) - 10) + number[-4:]  # изменяем часть цифр на *

    b = [number[i:i + 4] for i in
         range(0, len(number), 4)]  # получаем список из номера разделлных по 4 символа

    for el in b:
        string += el + " "

    return ''.join(number_list) + " " + string


def to_card_hide(recipient_number):
    """
    :param recipient_number: Принимаем значение по типу MasterCard 1234567890123456
    :return: Возвращаем MasterCard **3456
    """
    recipient_number = recipient_number
    recipient_number_list = recipient_number.split()  # преобразование входной строки в список
    number = recipient_number_list.pop(-1)  # забираем именно цифры

    number = "**" + number[-4:]
    return f"{''.join(recipient_number_list)} {number}"


def prepare_one_operation(date, id):
    receivin = date[id]

    correct_date = correct_format_date(receivin["date"])  # дата
    operation_amount = receivin["operationAmount"]["amount"]  # Сумма перевода
    name_operation = receivin["operationAmount"]["currency"]["name"]  # Валюта
    description_operation = receivin["description"]  # описание перевода
    to_operation = to_card_hide(receivin["to"])  # куда перевод
    if "from" in receivin:
        from_operation = from_card_hide(receivin["from"])  # откуда перевод
    else:
        from_operation = ""

    return correct_date, description_operation, from_operation, to_operation, operation_amount, name_operation,


def print_one_operation(date_str):
    """
    :param date_str: получаем одну операцию
    :return: Печать сообщения
    """
    date_str = date_str

    print(f"""{date_str[0]} {date_str[1]}
{date_str[2]} -> {date_str[3]}
{date_str[4]} {date_str[5]}""")
