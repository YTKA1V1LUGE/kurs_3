import class_print_messege


operation_json = class_print_messege.load_operation_json()
sort = class_print_messege.sort_operation(operation_json)
revers = class_print_messege.receiving_data(sort)
dates = class_print_messege.print_message(revers)
