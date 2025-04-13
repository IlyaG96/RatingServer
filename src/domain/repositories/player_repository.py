from abc import ABC, abstractmethod

from src.application.dto.player_dto import PlayerCreateDTO
from src.domain.entities.player import Player
from src.domain.value_objects.player_id import PlayerId


class PlayerRepository(ABC):

    @abstractmethod
    async def get_by_nickname(self, player_id: PlayerId) -> Player:
        pass

    @abstractmethod
    async def persist(self, player: Player) -> None:
        pass

    @abstractmethod
    async def create(self, player: PlayerCreateDTO) -> None:
        pass
