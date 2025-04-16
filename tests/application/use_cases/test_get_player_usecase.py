from unittest.mock import AsyncMock, Mock

from src.application.dto.player_dto import GetPlayerDTO
from src.application.use_cases.get_player import GetPlayer
from src.domain.exceptions.player import PlayerNotFoundError
from src.domain.value_objects.player.player_id import PlayerId


async def test_get_player_when_player_exists() -> None:
    mocked_player = Mock(nickname="test_nickname", rating=1000, player_id=PlayerId(value=1))
    mocked_repo = AsyncMock()
    mocked_repo.get_by_player_nickname = AsyncMock(return_value=mocked_player)

    use_case = GetPlayer(player_repository=mocked_repo)
    get_player_dto = GetPlayerDTO(nickname="test_nickname")

    result = await use_case.execute(get_player_dto)

    assert result.data is not None
    assert result.error is None
    assert result.data.nickname == "test_nickname"
    assert result.data.rating == 1000
    assert result.data.player_id == 1


async def test_get_player_when_player_does_not_exist() -> None:
    mocked_repo = Mock()
    mocked_repo.get_by_player_nickname = AsyncMock(side_effect=PlayerNotFoundError("Player not found"))

    use_case = GetPlayer(player_repository=mocked_repo)
    get_player_dto = GetPlayerDTO(nickname="test_nickname")

    result = await use_case.execute(get_player_dto)

    assert result.data is None
    assert result.error is not None
    assert result.error.details == "Player not found"
