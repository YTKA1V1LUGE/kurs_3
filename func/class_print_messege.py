import json
from datetime import datetime
import os


def load_operation_json():
    utils_path = os.path.dirname(__file__)
    operation_path = os.path.join(utils_path, "operations.json")
    with open(operation_path, "r", encoding="utf=8") as operation_file:
        return json.load(operation_file)


class account_transactions:
    def __init__(self, operation_json):
        """
        А что нужно прописывать в self?
        :param operation_json: список операция
        """
        self.date_operation = []  # список для смежных операций
        self.date = []  # список последних 5 операция
        self.load_operation_json = operation_json  # получение операций
        self.full_date_operation = []  # список для дат последних 5 операций
        self.id_operation = ""
        self.state_operation = ""
        self.operation_amount = ""
        self.name_operation = ""
        self.description_operation = ""
        self.from_operation = ""
        self.to_operation = ""
        self.correct_date = ""
        self.card_types = {
            "Visa Classic": (13, 6),  # 6 символов которые надо скрыть
            "MasterCard": (11, 6),
            "Maestro": (8, 6),
            "Счет": (5, 6),
            "Visa Gold": (10, 6),
            "Visa Platinum": (14, 6)
        }

    def __repr__(self):
        return "Класс для получения информации об операциях"

    def sort_operation(self):
        """

        :return: Список из дат последних 5 операций
        """
        self.full_date_operation = sorted(
            (operation["date"] for operation in self.load_operation_json if "date" in operation), reverse=True)[:5]
        return self.full_date_operation

    def correct_format_date(self, original_date):
        datetime_obj = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S.%f")
        correct_date = datetime_obj.strftime("%d.%m.%Y")
        return correct_date

    """
     def receiving_data(self):

    self.full_date_operation = self.sort_operation()
    for date in range(len(self.full_date_operation)): 
        for operation in self.load_operation_json:  
            if "date" in operation:
                if self.full_date_operation[date] == operation["date"]:
                    self.date.append(operation)
    return self.date
    """

    def receiving_data(self):
        """
        Функция для получениие 5 последних операций
        :return: список из последних 5 операций
        """
        self.full_date_operation = self.sort_operation()
        self.date = [operation for operation in self.load_operation_json
                     if operation.get("date") in self.full_date_operation]
        return self.date

    def from_card_hide(self, sender_number):
        string = ""
        for card_type, (start_index, end_index) in self.card_types.items():  # цикл в card_types
            if card_type in sender_number:  # если карта есть в списке
                sender_number = sender_number[:0] + sender_number[start_index:]  # получаем только цифры
                sender_number = sender_number[:-(len(sender_number) - 6)] + '*' * (len(sender_number) - 10) + sender_number[-4:]  # получаем значение по типу "124637******3588"
                b = [sender_number[i:i + 4] for i in range(0, len(sender_number), 4)]  # получаем список из номера разделлных по 4
                for el in b:
                    string += el + " "
                return f"{card_type} {string}"

    def to_card_hide(self, sender_number):
        for card_type, values in self.card_types.items():
            if card_type in sender_number:
                sender_number = "**" + sender_number[-4:]
                return f"{card_type} {sender_number}"

    def print_message(self):
        for operation in self.receiving_data():
            self.id_operation = operation["id"]  # id
            self.correct_date = self.correct_format_date(operation["date"]) #дата операции
            self.state_operation = operation["state"]  # Статус
            self.operation_amount = operation["operationAmount"]["amount"]  # Сумма перевода
            self.name_operation = operation["operationAmount"]["currency"]["name"]  # Валюта
            self.description_operation = operation["description"]  # описание перевода
            self.to_operation = self.to_card_hide(operation["to"])
            if "from" in operation:
                self.from_operation = self.from_card_hide(operation["from"])
            else:
                pass
            print(f"""{self.correct_date} {self.description_operation}
{self.from_operation} -> {self.to_operation}
{self.operation_amount} {self.name_operation}\n""")

"""
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
"""
