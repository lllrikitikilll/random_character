import re


def pars_json_character(char: dict) -> dict:
    """Парсит данные о персонаже"""

    pattern = r'^.*?\.\s*'
    data: list = char['msg'].split('\n')

    for i in range(len(data)):
        data[i] = re.sub(pattern, '', data[i])

    dct_data = {
        'sex': data[0],
        'age_childfree': data[1],
        'Physique': data[2],
        'profession': data[3],
        'health': data[4],
        'hobbies': data[5],
        'phobia': data[6],
        'character_trait': data[7],
        'luggage': data[8],
        'add_information': data[9],
        'card_1': data[10],
        'card_2': data[11],
    }

    dct_data['age_childfree'].replace('бык-осеменитель', 'Да')
    return dct_data
