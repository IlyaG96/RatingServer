from src.application.dto.player_dto import GetPlayerDTO, PlayerResponseDTO
from src.application.use_cases.base import Failure, Success, UseCase, UseCaseResult
from src.domain.exceptions.player import PlayerNotFoundError
from src.domain.repositories.player_repository import PlayerRepositoryInterface
from src.domain.value_objects.player.nickname import Nickname


class GetPlayer(UseCase):
    def __init__(self, player_repository: PlayerRepositoryInterface) -> None:
        self.player_repository = player_repository

    async def execute(self, get_player_dto: GetPlayerDTO) -> "UseCaseResult[PlayerResponseDTO, PlayerNotFoundError]":
        try:
            response = await self.player_repository.get_by_player_nickname(nickname=Nickname(get_player_dto.nickname))
            return Success(
                data=PlayerResponseDTO(
                    nickname=response.nickname, rating=response.rating, player_id=response.player_id.value
                ),
            )
        except PlayerNotFoundError as e:
            return Failure(error=e)
