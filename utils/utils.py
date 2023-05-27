from json import load


def open_file(file):
    with open(file, encoding='utf-8') as text:
        dict_ = load(text)
        return dict_


def get_last_operations(text, count=5):
    all_dates_list = []
    for i in text:
        if i != {} and i["state"] == "EXECUTED":
            all_dates_list.append(i['date'])
    all_dates_list.sort()
    all_dates_list = list(reversed(all_dates_list))
    dates_list = all_dates_list[:count]
    for i in text:
        if i != {} and i["state"] == "EXECUTED":
            if i['date'] in dates_list:
                index_ = dates_list.index(i['date'])
                dates_list[index_] = i
    return dates_list


def get_date(date):
    norm_date = date[:10]
    norm_date = norm_date.split('-')
    norm_date.reverse()
    return '.'.join(norm_date)


def get_from(from_who):
    from_who_list = from_who.split(' ')
    if len(from_who_list) > 2:
        card_number = from_who_list[-1]
        pay_system = ' '.join(from_who_list[:-1])
    else:
        card_number = from_who_list[1]
        pay_system = from_who_list[0]
    from_list = [pay_system, card_number]
    return from_list


def get_account_data(data):
    account_data = data[-1]
    if len(account_data) > 16:
        card_number = '**' + ''.join(account_data[-4:])
    else:
        card_number = (''.join(account_data[:4]) + ' ' +
                       ''.join(account_data[4:6]) + '** **** ' +
                       ''.join(account_data[-4:]))
    return card_number


def get_amount(operation_amount):
    finding_amount = operation_amount['amount'] + ' ' \
                    + operation_amount['currency']['name']
    return finding_amount
