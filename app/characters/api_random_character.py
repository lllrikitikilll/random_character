import requests
from character_utils import pars_json_character


# 'https://randomall.ru/api/gens/1723'
# 'https://randomall.ru/api/gens/1762'


def get_random_characters() -> dict:
    randomiser_character_url = 'https://randomall.ru/api/gens/1762'
    response = requests.post(randomiser_character_url)
    data = pars_json_character(response.json())
    print(data.items(), sep='\n')
    return response.json()



print(get_random_characters())