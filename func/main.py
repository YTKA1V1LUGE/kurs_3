import class_print_messege

message = class_print_messege

read_json = message.load_operation_json()
filter = message.filter_by_status(read_json)
sort = message.sort_operation(filter)

for i in range(len(sort)):
    prepare = message.prepare_one_operation(sort, i)
    message.print_one_operation(prepare)
    print()
"""08.12.2019 Открытие вклада
 -> Счет **5907
41096.24 USD

07.12.2019 Перевод организации
VisaClassic 2842 87** **** 9012  -> Счет **3655
48150.39 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568  -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет 3861 14** **** **** 9794  -> Счет **8125
62814.53 руб.

05.11.2019 Открытие вклада
 -> Счет **8381
21344.35 руб."""