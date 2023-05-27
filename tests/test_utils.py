import utils

def test_open_file():
    expected_result = [{"id": 441945886,
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
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
    }
    ]
    assert utils.open_file('/tests/test_text.json') == expected_result

def test_get_last_operations():
    pass
    # assert utils.get_last_operations()


def test_get_date():
    assert utils.get_date("2018-12-29T21:45:18.495053") == '29.12.2018'
    assert utils.get_date("2019-06-14T19:37:49.044089sssa") == '14.06.2019'


def test_get_from():
    assert utils.get_from("Счет 77977573135347241529") == ['Счет', '77977573135347241529']
    assert utils.get_from("MasterCard 1435442169918409") == ['MasterCard', '1435442169918409']
    assert utils.get_from("Visa Gold 7756673469642839") == ['Visa Gold', '7756673469642839']
def test_get_account_data():
    pass
def test_get_amount():
    pass



