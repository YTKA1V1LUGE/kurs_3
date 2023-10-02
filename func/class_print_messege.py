import json
from datetime import datetime
import os


def load_operation_json():
    utils_path = os.path.dirname(__file__)
    operation_path = os.path.join(utils_path, "operations.json")
    with open(operation_path, "r", encoding="utf=8") as operation_file:
        return json.load(operation_file)


def sort_operation(load_operation):
    """
    :return: Список из дат последних 5 операций
    """
    full_date_operation = sorted(
        (operation["date"] for operation in load_operation if "date" in operation), reverse=True)[:5]

    return full_date_operation


def correct_format_date(original_date):
    """
    :param original_date:  Получаем дату по типу 2022-01-01T12:00:00.000000
    :return: Возвращаем дату по типу 01.01.2022
    """
    datetime_obj = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S.%f")
    correct_date = datetime_obj.strftime("%d.%m.%Y")

    return correct_date


def receiving_data(date_operation):
    """
    Функция для получениие 5 последних операций
    :return: список из последних 5 операций
    """
    full_date_operation = date_operation
    date = [operation for operation in load_operation_json()
            if operation.get("date") in full_date_operation]

    return date


card_types = {
    "Visa Classic": (13, 6),  # 1 - сколько символов с строке, 6 символов которые надо скрыть
    "MasterCard": (11, 6),
    "Maestro": (8, 6),
    "Счет": (5, 6),
    "Visa Gold": (10, 6),
    "Visa Platinum": (14, 6)
}


def from_card_hide(sender_number):
    """
    :param sender_number: Получчаем значение карты по типу Visa Classic 1234567890123456
    :return: Возвращаем Visa Classic 1234 56** **** 3456
    """
    string = ""

    for card_type, (start_index, end_index) in card_types.items():  # цикл в card_types
        if card_type in sender_number:  # если карта есть в списке
            sender_number = sender_number[:0] + sender_number[start_index:]  # получаем только цифры
            sender_number = sender_number[:-(len(sender_number) - 6)] + '*' * (
                    len(sender_number) - 10) + sender_number[-4:]  # получаем значение по типу "124637******3588"

            b = [sender_number[i:i + 4] for i in
                 range(0, len(sender_number), 4)]  # получаем список из номера разделлных по 4

            for el in b:
                string += el + " "

            return f"{card_type} {string}"


def to_card_hide(sender_number):
    """
    :param sender_number: Принимаем значение по типу MasterCard 1234567890123456
    :return: Возвращаем MasterCard **3456
    """
    for card_type, values in card_types.items():
        if card_type in sender_number:
            sender_number = "**" + sender_number[-4:]

            return f"{card_type} {sender_number}"


def print_message(dates):
    """
    Функция для получение значений по операции и написания сообщения пользователю
    :return:
    """
    receivin = dates

    for operation in receivin:
        correct_date = correct_format_date(operation["date"])  # дата операции
        operation_amount = operation["operationAmount"]["amount"]  # Сумма перевода
        name_operation = operation["operationAmount"]["currency"]["name"]  # Валюта
        description_operation = operation["description"]  # описание перевода
        to_operation = to_card_hide(operation["to"])  # куда перевод

        if "from" in operation:
            from_operation = from_card_hide(operation["from"])  # откуда перевод
        else:
            from_operation = ""

        print(f"""{correct_date} {description_operation}
{from_operation} -> {to_operation}
{operation_amount} {name_operation}\n""")

