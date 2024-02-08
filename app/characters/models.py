from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base


class Character(Base):
    __tablename__ = 'character'

    id: Mapped[int] = mapped_column(primary_key=True)
    # user = ForeignKey('user.id')
    sex: Mapped[str] = mapped_column(String(255))
    age_childfree: Mapped[str] = mapped_column(String(255))
    Physique: Mapped[str] = mapped_column(String(255))
    profession: Mapped[str] = mapped_column(String(255))
    health: Mapped[str] = mapped_column(String(255))
    hobbies: Mapped[str] = mapped_column(String(255))
    phobia: Mapped[str] = mapped_column(String(255))
    character_trait: Mapped[str] = mapped_column(String(255))
    luggage: Mapped[str] = mapped_column(String(255))
    add_information: Mapped[str] = mapped_column(String(255))
    card_1: Mapped[str] = mapped_column(String(255))
    card_2: Mapped[str] = mapped_column(String(255))
    image: Mapped[str] = mapped_column(String(255))

