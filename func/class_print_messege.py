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


def sort_operation(load_operation):
    """
    :param load_operation: список операция
    :return: Список из последних 5 операций
    """
    load = load_operation
    sorted_lol = sorted(load, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)[:5]

    return sorted_lol


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
    number_list = sender_number.split()  # преобразование входной строки в список
    number = number_list.pop(-1)  # забираем именно цифры

    number = number[:6] + '*' * (len(number) - 10) + number[-4:]  # изменяем часть цифр на *

    hidden_number = ' '.join([number[i:i + 4] for i in range(0, len(number), 4)])  # разделяем номер по 4 символа

    return ''.join(number_list) + " " + hidden_number


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
