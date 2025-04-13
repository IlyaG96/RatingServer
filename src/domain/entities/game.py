from uuid import UUID

from pydantic import BaseModel, Field

from src.domain.repositories.game_repository import GameRepository
from src.domain.value_objects.game_result import GameResult
from src.domain.value_objects.player_id import PlayerId


class Game(BaseModel):
    game_id: UUID = Field(..., description="Уникальный идентификатор игры")
    player1_id: PlayerId = Field(
        ...,
    )
    player2_id: PlayerId = Field(
        ...,
    )
    result: GameResult = Field(..., description="Результат игры")

    async def save(self, repository: GameRepository) -> None:
        """Сохранение через репозиторий"""
        await repository.save(self)
