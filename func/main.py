import class_print_messege

message = class_print_messege

read_json = message.load_operation_json()
filter = message.filter_by_status(read_json)
sort = message.sort_operation(filter)

for i in range(len(sort)):
    prepare = message.prepare_one_operation(sort, i)
    message.print_one_operation(prepare)
    print()
