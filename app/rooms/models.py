from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Room(Base):
    __tablename__ = 'room'

    id: Mapped = mapped_column(primary_key=True)
    room_number: Mapped[int] = mapped_column(autoincrement=True)
    user_id: Mapped[int] = ForeignKey('user.id')
    password: Mapped[str] = mapped_column(String(255), nullable=True)
    Private: Mapped[bool] = mapped_column(Boolean())

