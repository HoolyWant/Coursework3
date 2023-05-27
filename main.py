import utils


FILE_NAME = 'operations.json'

text = utils.open_file(FILE_NAME)
last_operations = utils.get_last_operations(text)
for operation in last_operations:
    date = utils.get_date(operation['date'])
    description = operation['description']
    amount = utils.get_amount(operation['operationAmount'])
    if 'from' not in operation:
        from_data = ['']
        from_number = ''
    else:
        from_data = utils.get_from(operation['from'])
        from_number = utils.get_account_data(from_data)
    to_data = utils.get_from(operation['to'])
    to_number = utils.get_account_data(to_data)
    if 'from' not in operation:
        print(f'{date} {description}\n'
            f'{" ".join(to_data[:-1])} {to_number}\n'
            f'{amount}\n')
    else:
        print(f'{date} {description}\n'
            f'{from_data[0]} {from_number} -> {" ".join(to_data[:-1])} {to_number}\n'
            f'{amount}\n')





