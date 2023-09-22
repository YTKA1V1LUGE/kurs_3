#import func.class_print_messege
import json
from func import class_print_messege
import func

# как тесты писать то
load = class_print_messege.load_operation_json
function = class_print_messege.account_transactions(load)


def test_correct_format_date():
    assert function.correct_format_date("2019-12-03T04:27:03.427014") == "03.12.2019"


def test_sort_operation():
    assert function.sort_operation() == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890', '2019-12-03T04:27:03.427014', '2019-11-19T09:22:25.899614', '2019-11-13T17:38:04.800051']


"""
def test_load_operation_json():
    with open("../func/operations.json", "r", encoding="utf=8") as operation_file:
        js = json.load(operation_file)
    if js == load:
        print(js)
    else:
        print(0)
"""