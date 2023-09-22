import json
import datetime
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
        self.date_operation = []    # список для смежных операций
        self.date = []  # список последних 5 операция
        self.load_operation_json = operation_json   #   получение операций
        self.full_date_operation = []   # список для дат последних 5 операций
        self.id_operation = ""
        self.state_operation = ""
        self.operation_amount = ""
        self.name_operation = ""
        self.description_operation = ""
        self.from_operation = ""
        self.to_operation = ""
        self.correct_date = ""

    def __repr__(self):
        return "Класс для получения информации об операциях"

    def sort_operation(self):
        """
        :return: 5 последних операция
        """
        for operation in range(len(self.load_operation_json)):
            if "date" in self.load_operation_json[operation]:
                self.date_operation.append(self.load_operation_json[operation]["date"])
        self.date_operation.sort()
        self.full_date_operation = list(reversed(self.date_operation[-5:]))
        return self.full_date_operation

    """
    def correct_format_date(self, original_date):
        
        Скорее более хорошее, но если нужны именно точки то нижняя  функция
        :param original_date: Получаем дату по типу "2019-12-03T04:27:03.427014"
        :return: Дата по типу "2019-12-03"
        
        original_date = original_date.split("T")[0]
        #date_operation = datetime.datetime.strptime(original_date, '%Y-%m-%d') # я не знаю зачем
        #print(date_operation)
        return original_date
    """

    def correct_format_date(self, original_date):
        """
        :param original_date: Получаем дату по типу "2019-12-03T04:27:03.427014"
        :return: Дата по типу "2019-12-03"
        """
        correct_date = "".join(original_date)
        correct_date = correct_date.split("T")[0]
        correct_date = correct_date.split("-")
        year = correct_date[0]
        month = correct_date[1]
        days = correct_date[2]
        date = f"{days}.{month}.{year}"
        return date


    def receiving_data(self):
        """
        получение списка последних 5 операций
        :return: список последних 5 операция
        """
        self.full_date_operation = self.sort_operation()
        for date in range(len(self.full_date_operation)): # цикл с датами
            for operation in self.load_operation_json:  # цикл в джисон
                if "date" in operation:
                    if self.full_date_operation[date] == operation["date"]:
                        self.date.append(operation)
        return self.date

    def from_card_hide(self, sender_number):
        """
        Метод для того чтобы спрятать цифры карты
        :param sender_number: Получаем номер карты
        :return: Возвращаем номер карта по типу "2842 87** **** 9012"
        """
        string = "" # строка чтобы объединять цифры

        if "Visa Classic" in sender_number:
            sender_number = sender_number[:0] + sender_number[13:]
            sender_number = sender_number[:-(len(sender_number)-6)] + '*' * (len(sender_number)-10) + sender_number[-4:]
            b = [sender_number[i:i + 4] for i in range(0, len(sender_number), 4)]
            for el in b:
                string += el + " "
            return f"Visa Classic {string}"

        elif "MasterCard" in sender_number:
            sender_number = sender_number[:0] + sender_number[11:]
            sender_number = sender_number[:-(len(sender_number)-6)] + '*' * (len(sender_number)-10) + sender_number[-4:]
            b = [sender_number[i:i + 4] for i in range(0, len(sender_number), 4)]
            for el in b:
                string += el + " "
            return f"MasterCard {string}"

        elif "Maestro" in sender_number:
            sender_number = sender_number[:0] + sender_number[8:]
            sender_number = sender_number[:-(len(sender_number)-6)] + '*' * (len(sender_number)-10) + sender_number[-4:]
            b = [sender_number[i:i + 4] for i in range(0, len(sender_number), 4)]
            for el in b:
                string += el + " "
            return f"Maestro {string}"

        elif "Счет" in sender_number:
            sender_number = sender_number[:0] + sender_number[5:]
            sender_number = sender_number[:-(len(sender_number)-6)] + '*' * (len(sender_number)-10) + sender_number[-4:]
            b = [sender_number[i:i + 4] for i in range(0, len(sender_number), 4)]
            for el in b:
                string += el + " "

            return f"Счет {string}"

    def to_card_hide(self, sender_number):
        if "Счет" in sender_number:
            sender_number = "**" + sender_number[-4:]
            return f"Счет {sender_number}"
        elif "Visa Classic" in sender_number:
            sender_number = "**" + sender_number[-4:]
            return f"Visa Classic {sender_number}"

    def print_message(self):
        for operation in self.receiving_data():
            self.id_operation = operation["id"]  # id
            self.correct_date = self.correct_format_date(operation["date"])
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
