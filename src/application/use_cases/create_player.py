from src.application.dto.player_dto import PlayerCreateDTO
from src.domain.repositories.player_repository import PlayerRepository
from src.infrastructure.database.async_database import database
from src.infrastructure.database.repositories.player_repository import PlayerRepositorySQLAlchemy


class CreatePlayerUseCase:
    def __init__(self, player_repository: PlayerRepository = PlayerRepositorySQLAlchemy(base=database)):
        self.player_repository = player_repository

    async def execute(self, player_create_dto: PlayerCreateDTO) -> None:
        await self.player_repository.create(player_create_dto)

