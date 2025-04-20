import pytest

from src.infrastructure.database.async_database import SQLAlchemyDataBase
from src.infrastructure.database.models.base import Base  # noqa: F401
from src.infrastructure.database.repositories.player_repository import PlayerRepository

@pytest.fixture(scope="function")
def player_repository(database: SQLAlchemyDataBase) -> PlayerRepository:
    """Fixture to create a PlayerRepository instance."""
    return PlayerRepository(database=database)