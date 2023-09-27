import class_print_messege

"""
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
"""

operation_json = class_print_messege.load_operation_json()
sort = class_print_messege.sort_operation(operation_json)
revers = class_print_messege.receiving_data(sort)
dates = class_print_messege.print_message(revers)
