import pytest

from src.domain.exceptions.player import PlayerAlreadyExistsError
from src.domain.value_objects.player.nickname import Nickname
from src.domain.value_objects.player.player_creation_data import PlayerCreationData
from src.domain.value_objects.player.rating import Rating
from src.infrastructure.database.repositories.player_repository import PlayerRepository


async def test_add_player_success(player_repository: PlayerRepository) -> None:
    """Тест успешного добавления нового игрока."""
    nickname = Nickname("test_add_success")
    player_data = PlayerCreationData(nickname=nickname)
    await player_repository.create(player_data)
    added_player = await player_repository.get_by_player_nickname(nickname)

    assert added_player is not None
    assert added_player.nickname == player_data.nickname
    assert added_player.rating == Rating(1000)


async def test_add_player_duplicate_nickname(player_repository: PlayerRepository) -> None:
    """Тест: добавление игрока с дублирующимся никнеймом вызывает PlayerAlreadyExistsError."""
    nickname = Nickname("test_add_duplicate")
    player_data1 = PlayerCreationData(nickname=nickname)
    await player_repository.create(player_data1)  # Добавляем первого игрока

    player_data2 = PlayerCreationData(nickname=nickname)
    # Ожидаем исключение при попытке добавить дубликат
    with pytest.raises(PlayerAlreadyExistsError):
        await player_repository.create(player_data2)
