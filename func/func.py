import json
import datetime


def load_operation_json():
    """
    :return: Возвращение списка операция
    """
    with open("operations.json", "r", encoding="utf=8") as operation_file:
        return json.load(operation_file)


class account_transactions:
    def __init__(self):
        self.load_operation_json = load_operation_json()
        self.full_date_operation = []
        self.date_operation = []
        self.correct_date_operation = []
        self.dates = []

    def __repr__(self):
        return "Класс для выводасообщения об операциях"

    def sort_operation(self):
        """
        Сортировка и получение последних 5 операция
        :return: Последние 5 операция
        """
        for operation in self.load_operation_json:
            if "date" in operation:
                self.date_operation.append(operation["date"])
        self.date_operation.sort()
        return list(reversed(self.date_operation[-5:]))

        """
    def correct_date(self):
        """
        # Функция для возврата даты по типу ДЕНЬ.Месяц.Год
        #:return: корректный формат даты
        """
        self.full_date_operation = self.sort_operation()
        for dates in self.full_date_operation:
            date = "".join(dates)
            date = date.split("T")[0]
            date = date.split("-")
            year = date[0]
            month = date[1]
            days = date[2]
            date = f"{days}.{month}.{year}"
            self.dates.append(date)
        return self.dates
        """

    def correct_date(self):
        #" Скорее более лаконичное использование, но если нужны именно точки то верхняя функция "
        self.full_date_operation = self.sort_operation()# (sort_operation(self)[1])
        for days in self.full_date_operation:
            self.correct_date_operation.append(days.split("T")[0])
        '''for i in self.correct_date_operation:
            date_operation = datetime.datetime.strptime(i, '%Y-%m-%d').date()''' # я не знаю как и зачем
        return self.correct_date_operation

    def correct_format(self):
        full_date_operation = self.correct_date()
        for operation in self.load_operation_json:
            #   if "date" in operation:
            if operation["date"] == self.full_date_operation[0]:
                id_operation = operation["id"]  # id
                state_operation = operation["state"]  # Статус
                operation_amount = (operation["operationAmount"])["amount"]  # Сумма перевода
                name_operation = (operation["operationAmount"])["currency"]["name"]  # Валюта
                description_operation = operation["description"]  # описание перевода
                from_operation = operation["from"]
                to_operation = operation["to"]
                return id_operation, state_operation, operation_amount, name_operation, description_operation, from_operation, to_operation


a = account_transactions()
print(a.correct_format())
