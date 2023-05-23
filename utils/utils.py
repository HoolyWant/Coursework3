from json import load


def open_file(file):
    with open(file, encoding='utf-8') as text:
        dict_ = load(text)
        return dict_

# def last_operations_dates(text):
#     dates_list = []
#     for i in text:
#         if i['state'] == 'EXECUTED':
#             date = i['date'][:10]
#             date_list = date.split('-')
#             date_list.reverse()
#             dates_list.append('.'.join(date_list))
#     dates_list.sort()
#     return dates_list
# #


def get_last_operations(text, count=5):
    all_dates_list = [i['date'] for i in text if i != {}]
    all_dates_list.sort()
    all_dates_list = list(reversed(all_dates_list))
    dates_list = all_dates_list[:count]

    list_for_operations = []
    for i in text:
        if i != {} and i["state"] == "EXECUTED":
            if i['date'] in dates_list:
                list_for_operations.append(i)


    # for i in list_for_operations:
    #     index_ = dates_list.index(i['date'])
    #     dates_list[index_] = i
    # return dates_list
    return list_for_operations







