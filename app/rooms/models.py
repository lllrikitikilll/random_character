from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

class Room(Base):
    __tablename__ = 'room'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_number: Mapped[int] = mapped_column(autoincrement=True)
    password: Mapped[str] = mapped_column(String(255), nullable=True)
    Private: Mapped[bool] = mapped_column(Boolean())

    user = relationship('User', back_populates='rooms')
