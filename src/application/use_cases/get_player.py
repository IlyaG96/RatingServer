from src.application.dto.player_dto import GetPlayerDTO
from src.application.use_cases.base import UseCase, UseCaseResult
from src.domain.exceptions.player import PlayerNotFoundError
from src.domain.repositories.player_repository import PlayerRepositoryInterface
from src.domain.value_objects.player.nickname import Nickname
from src.infrastructure.api.schemas.player import PlayerResponse


class GetPlayerResult(UseCaseResult):
    result: PlayerResponse | None
    error: PlayerNotFoundError | None


class GetPlayer(UseCase):
    def __init__(self, player_repository: PlayerRepositoryInterface) -> None:
        self.player_repository = player_repository

    async def execute(self, get_player_dto: GetPlayerDTO) -> GetPlayerResult:
        try:
            response = await self.player_repository.get_by_player_nickname(nickname=Nickname(get_player_dto.nickname))
            return GetPlayerResult(
                result=PlayerResponse(
                    nickname=response.nickname, rating=response.rating, player_id=response.player_id.value
                ),
                error=None,
            )
        except PlayerNotFoundError as e:
            return GetPlayerResult(result=None, error=e)
