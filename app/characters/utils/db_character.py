from core.database import session_maker
from app.characters.models import Character

def add_character_to_db(data: dict) -> None:
    with session_maker() as session:
        session.add(Character(**data))
        session.commit()
