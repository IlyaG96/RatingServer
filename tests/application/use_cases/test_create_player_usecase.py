from unittest.mock import AsyncMock

from src.application.dto.player_dto import CreatePlayerDTO
from src.application.use_cases.create_player import CreatePlayer
from src.domain.exceptions.player import PlayerAlreadyExistsError
from src.domain.value_objects.player.player_creation_data import PlayerCreationData


async def test_create_player_success() -> None:
    # Arrange
    mocked_repo = AsyncMock()
    mocked_repo.create = AsyncMock()

    use_case = CreatePlayer(player_repository=mocked_repo)
    create_player_dto = CreatePlayerDTO(nickname="test_nickname")

    # Act
    result = await use_case.execute(create_player_dto)

    # Assert
    assert result.data is True
    assert result.error is None
    mocked_repo.create.assert_called_once()
    # Verify that the correct PlayerCreationData was passed to the repository
    call_args = mocked_repo.create.call_args[0][0]
    assert isinstance(call_args, PlayerCreationData)
    assert call_args.nickname == "test_nickname"


async def test_create_player_with_duplicate_nickname() -> None:
    # Arrange
    mocked_repo = AsyncMock()
    mocked_repo.create = AsyncMock(side_effect=PlayerAlreadyExistsError("Player already exists"))

    use_case = CreatePlayer(player_repository=mocked_repo)
    create_player_dto = CreatePlayerDTO(nickname="test_nickname")

    # Act
    result = await use_case.execute(create_player_dto)

    # Assert
    assert result.data is None
    assert result.error is not None
    assert isinstance(result.error, PlayerAlreadyExistsError)
