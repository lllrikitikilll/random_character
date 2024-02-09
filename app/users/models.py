from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(60))

    room = relationship('Room', back_populates='users')
