#import func.class_print_messege
import json
from func import class_print_messege
import func

# как тесты писать то
load = class_print_messege.load_operation_json
function = class_print_messege.account_transactions(load)

def test_correct_format_date():
    assert function.correct_format_date("2019-12-03T04:27:03.427014") == "03.12.2019"

def test_load_operation_json():
    with open("/home/ytka/py/kurs_3/func/operations.json", "r", encoding="utf=8") as operation_file:
        js = json.load(operation_file)
    assert js == load


#qwe = class_print_messege.load_operation_json()
#print(qwe)

