from sqlalchemy import UUID, Enum, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.value_objects.game.game_result import GameResult
from src.infrastructure.database.models.base import Base


class GameModel(Base):
    __tablename__ = "games"
    game_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False)
    player1_id: Mapped[int] = mapped_column(Integer, nullable=False)
    player2_id: Mapped[int] = mapped_column(Integer, nullable=False)
    result: Mapped[GameResult] = mapped_column(Enum(GameResult), nullable=False)
