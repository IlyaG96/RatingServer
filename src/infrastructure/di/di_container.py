from configuration import DATABASE_URL
from src.infrastructure.database.async_database import SQLAlchemyDataBase
from src.infrastructure.database.repositories.player_repository import PlayerRepository


class DependencyContainer:
    def __init__(self) -> None:
        self._database = SQLAlchemyDataBase(DATABASE_URL)
        self._player_repository = PlayerRepository(self._database)

    @property
    def player_repository(self) -> PlayerRepository:
        return self._player_repository


dependency_container = DependencyContainer()
