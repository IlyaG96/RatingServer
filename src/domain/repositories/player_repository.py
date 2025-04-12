from abc import ABC, abstractmethod

from src.domain.entities.player import Player


class PlayerRepository(ABC):
    @abstractmethod
    async def get_by_nickname(self, player_id: int) -> Player:
        pass

    @abstractmethod
    async def save(self, player: Player) -> None:
        pass
