from dataclasses import dataclass

from src.application.dto.player_dto import CreatePlayerDTO
from src.application.use_cases.base import UseCase, UseCaseResult
from src.domain.exceptions.player import PlayerAlreadyExistsError
from src.domain.repositories.player_repository import PlayerRepositoryInterface
from src.domain.value_objects.player.nickname import Nickname
from src.domain.value_objects.player.player_creation_data import PlayerCreationData


@dataclass(frozen=True)
class CreatePlayerResult(UseCaseResult):
    data: bool | None
    error: PlayerAlreadyExistsError | None


class CreatePlayer(UseCase):
    def __init__(self, player_repository: PlayerRepositoryInterface) -> None:
        self.player_repository = player_repository

    async def execute(self, player_create_dto: CreatePlayerDTO) -> CreatePlayerResult:
        try:
            player_creation_data = PlayerCreationData(nickname=Nickname(player_create_dto.nickname))
            await self.player_repository.create(player_creation_data)
            return CreatePlayerResult(data=True, error=None)
        except PlayerAlreadyExistsError as e:
            return CreatePlayerResult(data=None, error=e)
