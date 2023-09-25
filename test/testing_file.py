import pytest
from func import class_print_messege

operation_json = [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }]

account = class_print_messege.account_transactions(operation_json)


def test_correct_format_date():
    original_date = "2022-01-01T12:00:00.000000"
    expected_result = "01.01.2022"
    assert account.correct_format_date(original_date) == expected_result


def test_sort_operation():
    expected_result = ['2019-08-26T10:50:58.294041', "2019-07-03T18:35:29.512364"]
    assert account.sort_operation() == expected_result


def test_receiving_data():
    expected_result = operation_json[0]
    assert account.receiving_data()[0] == expected_result


def test_from_card_hide():
    sender_number = "Visa Classic 1234567890123456"
    expected_result = "Visa Classic 1234 56** **** 3456 "
    assert account.from_card_hide("") is None
    assert account.from_card_hide(sender_number) == expected_result


def test_to_card_hide():
    sender_number = "MasterCard 1234567890123456"
    expected_result = "MasterCard **3456"
    assert account.to_card_hide(sender_number) == expected_result


def test_print_message(capsys):
    account.print_message()
    captured = capsys.readouterr()
    expected_output = """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199  -> Счет **9589
31957.58 руб.

03.07.2019 Перевод организации
MasterCard 7158 30** **** 6758  -> Счет **5560
8221.37 USD
\n"""
    assert captured.out == expected_output


# Run the tests
pytest.main()
