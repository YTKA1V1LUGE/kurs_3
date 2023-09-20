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
        self.full_date_operation = None
        self.date_operation = []
        self.correct_date_operation = []
        self.dates = []
        self.from_operation = None
        self.id_operation = []
        self.state_operation = []
        self.operation_amount = []
        self.name_operation = []
        self.description_operation = []
        self.to_operation = []
        self.date_for_calculation = None # переменная чтобы не вызывать посстояно correct_date
        self.opera = -1
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
        return self.correct_date_operation, self.full_date_operation

    """
    def correct_format(self):
        self.full_date_operation = self.correct_date()[1]
        for operation in self.load_operation_json:
            if "date" in operation:
                if operation["date"] == self.full_date_operation[1]:
                    self.id_operation = operation["id"]  # id
                    state_operation = operation["state"]  # Статус
                    operation_amount = (operation["operationAmount"])["amount"]  # Сумма перевода
                    name_operation = (operation["operationAmount"])["currency"]["name"]  # Валюта
                    description_operation = operation["description"]  # описание перевода
                    if "from" in operation:
                        self.from_operation = operation["from"]
                    else:
                        pass
                    self.to_operation.append(operation["to"])
                    return self.id_operation, state_operation, operation_amount, name_operation, description_operation, self.from_operation, self.to_operation
    """
    """
    def correct_format(self):
        self.date_for_calculation = self.correct_date() # хрень чтобы получать даты
        self.full_date_operation = self.date_for_calculation[1] # хрень чтобы получать полную дату
        for operation in self.load_operation_json: #цикл в джисон
            opera = 0   # счетчик для списка
            while opera != len(self.full_date_operation)-1: #ААААААААА
                opera += 1
            #if "date" in operation:
                if operation["date"] == self.full_date_operation[opera]:
                    opera += 1
                    #print(self.full_date_operation)
                    self.id_operation = operation["id"]  # id
                    self.state_operation.append(operation["state"])  # Статус
                    self.operation_amount.append(operation["operationAmount"]["amount"])  # Сумма перевода
                    self.name_operation.append(operation["operationAmount"]["currency"]["name"])  # Валюта
                    self.description_operation.append(operation["description"])  # описание перевода
                    if "from" in operation:
                        self.from_operation.append(operation["from"])
                    else:
                        pass
                    self.to_operation.append(operation["to"])
                    return self.id_operation, self.state_operation, self.operation_amount, self.name_operation, self.description_operation, self.from_operation, self.to_operation
    """
    """
    def correct_format(self, opera):
        self.date_for_calculation = self.correct_date() # хрень чтобы получать даты
        #self.full_date_operation = self.date_for_calculation[1][4] # ->
     #   Как получается так что если поменять цифру во второй квадратной скобке, например на 0 он выводит лишь одинаковые числа
        for operation in self.load_operation_json:  # цикл в джисон
                self.full_date_operation = self.date_for_calculation[1]
                self.full_date_operation = self.full_date_operation[opera]
                #print(self.full_date_operations)
                #print(opera)
                if operation["date"] == self.full_date_operation:
                    self.id_operation = operation["id"]  # id
                    self.state_operation = operation["state"]  # Статус
                    self.operation_amount = operation["operationAmount"]["amount"]  # Сумма перевода
                    self.name_operation = operation["operationAmount"]["currency"]["name"]  # Валюта
                    self.description_operation = operation["description"]  # описание перевода
                    if "from" in operation:
                        self.from_operation = operation["from"]
                    else:
                        pass
                    self.to_operation = operation["to"]
                    return self.date_for_calculation[0][opera], self.id_operation, self.state_operation, self.operation_amount, self.name_operation, self.description_operation, self.from_operation, self.to_operation
    """
    def correct_format(self):
        self.date_for_calculation = self.correct_date()  # хрень чтобы получать даты +
        self.full_date_operation = self.date_for_calculation[1]  # +
        dates = []
        for date in self.full_date_operation:
            while len(dates) != 5:
                print(1)
                dates.append(date)
                pass
            pass

        #for operation in self.load_operation_json:  # цикл в джисон +
            #if "date" in operation:
                    #if date == operation["date"]:
                        #print(operation["date"])
                        #dates.append(operation)
        #return dates



a = account_transactions()


#print(a.correct_format())
qwerty = []
opera = 0
while opera != 5:
    #print(opera)
    qwerty.append(a.correct_format())
    opera += 1
#print(qwerty)
#for i in qwerty:
#    print(i)
