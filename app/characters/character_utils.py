import re


def pars_json_character(char: dict) -> dict:
    """Парсит данные о персонаже"""
    pattern = r'^.*?:\s*'
    data: list = char['msg'].replace('\n', ', ').split(', ')
    for i in range(len(data)):
        data[i] = re.sub(pattern, '', data[i])


    dct_data = {
        'sex': data[0],
        'age': data[1],
        'childfree': data[2],
        'health': data[3],
        'phobia': data[4],
        'profession': data[5],
        'hobbies': data[6],
        'small_luggage': data[7],
        'large_luggage': data[8],
        'add_information': data[9],
        'card_1': data[10],
        'card_2': data[11],
    }
    return dct_data
