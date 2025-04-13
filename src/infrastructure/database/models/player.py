from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import Base


class PlayerModel(Base):
    __tablename__ = "players"
    player_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    rating: Mapped[int] = mapped_column(default=1000, nullable=False)
