from abc import ABC, abstractmethod

from src.domain.entities.game import Game
from src.domain.value_objects.game_id import GameId


class GameRepository(ABC):
    @abstractmethod
    async def save(self, game: Game) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, game_id: GameId) -> Game:
        pass
