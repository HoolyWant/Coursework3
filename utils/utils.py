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
    norm_date.split('-')
    norm_date .reverse()
    '.'.join(norm_date )
    return norm_date
