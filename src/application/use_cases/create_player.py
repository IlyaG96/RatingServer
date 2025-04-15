from src.application.dto.player_dto import PlayerCreateDTO
from src.domain.repositories.player_repository import PlayerRepositoryInterface


class CreatePlayerUseCase:
    def __init__(self, player_repository: PlayerRepositoryInterface) -> None:
        self.player_repository = player_repository

    async def execute(self, player_create_dto: PlayerCreateDTO) -> None:
        await self.player_repository.create(player_create_dto)
