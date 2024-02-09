import requests
from app.characters.utils.character_utils import pars_json_character
from app.characters.schemas import CharacterDTO

# 'https://randomall.ru/api/gens/1723'
# 'https://randomall.ru/api/gens/1762'


def get_random_characters() -> CharacterDTO:
    """Возвращает характеристики персонажа"""

    randomiser_character_url = 'https://randomall.ru/api/gens/1723'
    response = requests.post(randomiser_character_url)
    data_character = pars_json_character(response.json())
    return CharacterDTO(**data_character)
