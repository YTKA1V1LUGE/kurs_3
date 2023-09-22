# import func.class_print_messege
import json
from func import class_print_messege
import func

# где- то еще проверку есть ли фром ли нет
load = {'date': '2019-11-13T17:38:04.800051',
        'description': 'Перевод со счета на счет',
        'from': 'Счет 38611439522855669794',
        'id': 482520625,
        'operationAmount': {'amount': '62814.53',
                            'currency': {'code': 'RUB', 'name': 'руб.'}},
        'state': 'EXECUTED',
        'to': 'Счет 46765464282437878125'}



function = class_print_messege.account_transactions(class_print_messege.load_operation_json())


def test_correct_format_date():  ###
    assert function.correct_format_date("2019-11-13T17:38:04.800051") == "13.11.2019"


def test_sort_operation():
    assert function.sort_operation()[4] == '2019-11-13T17:38:04.800051'


def test_receiving_data():
    assert function.receiving_data()[4] == load


def test_from_card_hide():
    assert function.from_card_hide("Счет 38611439522855669794") == "Счет 3861 14** **** **** 9794 "


def test_to_card_hide():
    assert function.to_card_hide("Счет 46765464282437878125") == "Счет **8125"


def test_print_message():
    assert function.print_message() == None


"""
def test_load_operation_json():
    with open("../func/operations.json", "r", encoding="utf=8") as operation_file:
        js = json.load(operation_file)
    if js == load:
        print(js)
    else:
        print(0)
"""
