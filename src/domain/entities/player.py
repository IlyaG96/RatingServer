from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from src.domain.value_objects.nickname import Nickname
from src.domain.value_objects.player_id import PlayerId
from src.domain.value_objects.rating import Rating


if TYPE_CHECKING:
    from src.domain.repositories.player_repository import PlayerRepository


class Player(BaseModel):
    player_id: PlayerId = Field(..., description="Уникальный ID игрока")
    rating: Rating = Field(..., description="Рейтинг игрока")
    nickname: Nickname = Field(..., description="Никнейм игрока")

    def update_rating(self, new_rating: int) -> None:
        """Обновление рейтинга игрока."""
        self.rating = new_rating

    async def persist(self, repository: 'PlayerRepository') -> None:
        """Сохранение через репозиторий."""
        await repository.persist(self)
