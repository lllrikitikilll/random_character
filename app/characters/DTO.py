from pydantic import BaseModel


class CharacterDTO(BaseModel):
    sex: str
    age_childfree: str
    Physique: str
    profession: str
    health: str
    hobbies: str
    phobia: str
    character_trait: str
    luggage: str
    add_information: str
    card_1: str
    card_2: str
