import pytest
from func import class_print_messege


def operation_json():
    return [{
        "id": 441945886,
        "state": "CANCELED",
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
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
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
        }
    ]


@pytest.fixture(name="operation_json")
def operation_json_fixture():
    return operation_json()


@pytest.fixture
def sender_number():
    return "Visa Classic 1234567890123456"


@pytest.fixture
def recipient_number():
    return "MasterCard 1234567890123456"


@pytest.fixture
def original_date():
    return "2022-01-01T12:00:00.000000"


def test_from_card_hide(sender_number):
    expected_result = "Visa Classic 1234 56** **** 3456"
    assert class_print_messege.from_card_hide(sender_number) == expected_result


def test_to_card_hide(recipient_number):
    expected_result = "MasterCard **3456"
    assert class_print_messege.to_card_hide(recipient_number) == expected_result


def test_correct_format_date(original_date):
    expected_result = "01.01.2022"
    assert class_print_messege.correct_format_date(original_date) == expected_result


def test_filter_by_status(operation_json):
    """
    :param operation_json:  список операций
    :return: Должны возвращаться лишь выполнение операции
    """
    expected_result = [{'date': '2018-12-28T23:10:35.459698',
                        'description': 'Открытие вклада',
                        'id': 172864002,
                        'operationAmount': {'amount': '49192.52',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 96231448929365202391'},
                       {'date': '2019-07-03T18:35:29.512364',
                        'description': 'Перевод организации',
                        'from': 'MasterCard 7158300734726758',
                        'id': 41428829,
                        'operationAmount': {'amount': '8221.37',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 35383033474447895560'}]

    assert class_print_messege.filter_by_status(operation_json) == expected_result


def test_sort_operation(operation_json):
    expected_result = [{'date': '2019-07-03T18:35:29.512364',
                        'description': 'Перевод организации',
                        'from': 'MasterCard 7158300734726758',
                        'id': 41428829,
                        'operationAmount': {'amount': '8221.37',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 35383033474447895560'},
                       {'date': '2018-12-28T23:10:35.459698',
                        'description': 'Открытие вклада',
                        'id': 172864002,
                        'operationAmount': {'amount': '49192.52',
                                            'currency': {'code': 'USD', 'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 96231448929365202391'}]

    filter = class_print_messege.filter_by_status(operation_json)

    assert class_print_messege.sort_operation(filter) == expected_result


def test_prepare_one_operation(operation_json):
    filter = class_print_messege.filter_by_status(operation_json)
    sort = class_print_messege.sort_operation(filter)
    prepare = class_print_messege.prepare_one_operation(sort, 0)

    assert prepare == ('03.07.2019',
                       'Перевод организации',
                       'MasterCard 7158 30** **** 6758',
                       'Счет **5560',
                       '8221.37',
                       'USD')


def test_print_one_operation(capsys, operation_json):
    filter = class_print_messege.filter_by_status(operation_json)
    sort = class_print_messege.sort_operation(filter)

    for i in range(len(sort)):
        prepare = class_print_messege.prepare_one_operation(sort, i)
        class_print_messege.print_one_operation(prepare)
        print()

    captured = capsys.readouterr()
    expected_output = ('03.07.2019 Перевод организации\n'
                       'MasterCard 7158 30** **** 6758 -> Счет **5560\n'
                       '8221.37 USD\n'
                       '\n'
                       '28.12.2018 Открытие вклада\n'
                       ' -> Счет **2391\n'
                       '49192.52 USD\n'
                       '\n')

    assert captured.out == expected_output


pytest.main()
