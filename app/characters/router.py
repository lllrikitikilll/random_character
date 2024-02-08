import time

from fastapi import APIRouter

from app.characters.schemas import SCharacter
from app.characters.utils.api_images import run_generate
from app.characters.utils.api_random_character import get_random_characters
from app.characters.utils.db_character import add_character_to_db

router = APIRouter(
    prefix='/api',
    tags=['character']
)


@router.get('/create')
async def create_character() -> SCharacter:
    """Создание персонажа"""

    prompt = get_random_characters()
    image_name = str(time.time_ns())
    prompt['image'] = image_name
    await run_generate(prompt, image_name)
    add_character_to_db(prompt)
    return SCharacter(**prompt)
