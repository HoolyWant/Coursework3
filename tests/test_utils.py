import utils


def test_get_last_operations():
    assert utils.get_last_operations([{'date': '12.02', 'state': 'EXECUTED'}]) == \
            [{'date': '12.02', 'state': 'EXECUTED'}]
    assert utils.get_last_operations([{'date': '12.02', 'state': 'CANCELED'}]) == []
    assert utils.get_last_operations([{}]) == []


def test_get_date():
    assert utils.get_date("2018-12-29T21:45:18.495053") == '29.12.2018'
    assert utils.get_date("2019-06-14T19:37:49.044089sssa") == '14.06.2019'


def test_get_from():
    assert utils.get_from("Счет 77977573135347241529") == ['Счет', '77977573135347241529']
    assert utils.get_from("MasterCard 1435442169918409") == ['MasterCard', '1435442169918409']
    assert utils.get_from("Visa Gold 7756673469642839") == ['Visa Gold', '7756673469642839']


def test_get_account_data():
    assert utils.get_account_data(['Счет', '77977573135347241529']) == '**1529'
    assert utils.get_account_data(['MasterCard', '1435442169918409']) == '1435 44** **** 8409'
    assert utils.get_account_data(['Visa Gold', '7756673469642839']) == '7756 67** **** 2839'


def test_get_amount():
    assert utils.get_amount({"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}}) == "97853.86 руб."

