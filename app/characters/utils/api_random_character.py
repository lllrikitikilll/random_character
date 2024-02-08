from pprint import pprint

import requests
from app.characters.utils.character_utils import pars_json_character


# 'https://randomall.ru/api/gens/1723'
# 'https://randomall.ru/api/gens/1762'


def get_random_characters() -> dict:
    randomiser_character_url = 'https://randomall.ru/api/gens/1723'
    response = requests.post(randomiser_character_url)
    data = pars_json_character(response.json())
    data['age_childfree'].replace('бык-осеменитель', 'Да')
    return data
