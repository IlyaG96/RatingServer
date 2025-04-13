from sqlalchemy import Integer, UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
from src.domain.entities.game import GameResult
from src.domain.value_objects.game_id import GameId
from src.domain.value_objects.player_id import PlayerId
from src.infrastructure.database.models.base import Base


class GameModel(Base):
    __tablename__ = "games"
    game_id: Mapped[GameId] = mapped_column(UUID, primary_key=True, nullable=False)
    player1_id: Mapped[PlayerId] = mapped_column(Integer, nullable=False)
    player2_id: Mapped[PlayerId] = mapped_column(Integer, nullable=False)
    result: Mapped[GameResult] = mapped_column(Enum(GameResult), nullable=False)
