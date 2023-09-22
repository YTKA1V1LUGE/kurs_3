"""
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
"""
import class_print_messege

messedge_operasion = class_print_messege.account_transactions(class_print_messege.load_operation_json())
messedge_operasion.print_messenge()