from abc import ABC, abstractmethod

from src.domain.entities.player import Player
from src.domain.value_objects.player.nickname import Nickname
from src.domain.value_objects.player.player_creation_data import PlayerCreationData
from src.domain.value_objects.player.player_id import PlayerId


class PlayerRepositoryInterface(ABC):
    @abstractmethod
    async def get_by_player_id(self, player_id: PlayerId) -> Player:
        pass

    @abstractmethod
    async def get_by_player_nickname(self, nickname: Nickname) -> Player:
        pass

    @abstractmethod
    async def persist(self, player: Player) -> None:
        pass

    @abstractmethod
    async def create(self, player: PlayerCreationData) -> None:  # FIXME
        pass
