import asyncio
import logging

import pytest

from src.domain.exceptions.player import PlayerAlreadyExistsError
from src.domain.value_objects.player.nickname import Nickname
from src.domain.value_objects.player.player_creation_data import PlayerCreationData
from src.domain.value_objects.player.rating import Rating
from src.infrastructure.database.repositories.player_repository import PlayerRepository

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

async def test_add_player_success(player_repository: PlayerRepository):
    """Тест успешного добавления нового игрока."""
    nickname = Nickname("test_add_success")
    logger.debug(f"Running test_add_player_success in loop: {asyncio.get_running_loop()}")
    player_data = PlayerCreationData(nickname=nickname)
    await player_repository.create(player_data)
    added_player = await player_repository.get_by_player_nickname(nickname)

    assert added_player is not None
    assert added_player.nickname == player_data.nickname
    assert added_player.rating == Rating(1000)

async def test_add_player_duplicate_nickname(player_repository: PlayerRepository):
    logger.debug(f"Running test_add_player_duplicate_nickname in loop: {asyncio.get_running_loop()}")

    """Тест: добавление игрока с дублирующимся никнеймом вызывает PlayerAlreadyExistsError."""
    nickname = Nickname("test_add_duplicate")
    player_data1 = PlayerCreationData(nickname=nickname)
    await player_repository.create(player_data1) # Добавляем первого игрока

    player_data2 = PlayerCreationData(nickname=nickname)
    # Ожидаем исключение при попытке добавить дубликат
    with pytest.raises(PlayerAlreadyExistsError):
        await player_repository.create(player_data2)


# async def test_get_player_by_id_success(player_repository: PlayerRepository, db_session: AsyncSession):
#     """Тест успешного получения существующего игрока по ID."""
#     nickname = Nickname("test_get_id_success")
#     added_player = await player_repository.create(PlayerCreationData(nickname=nickname))
#
#     fetched_player = await player_repository.get_by_player_id(added_player.id)
#
#     assert fetched_player is not None
#     assert fetched_player.id == added_player.id
#     assert fetched_player.nickname == nickname
#
#
# async def test_get_player_by_id_not_found(player_repository: PlayerRepository):
#     """Тест: получение несуществующего игрока по ID вызывает PlayerNotFoundError."""
#     non_existent_id = PlayerId() # Генерируем случайный UUID
#     with pytest.raises(PlayerNotFoundError):
#         await player_repository.get_by_player_id(non_existent_id)
#
#
# async def test_get_player_by_nickname_success(player_repository: PlayerRepository, db_session: AsyncSession):
#     """Тест успешного получения существующего игрока по никнейму."""
#     nickname = Nickname("test_get_nick_success")
#     added_player = await player_repository.create(PlayerCreationData(nickname=nickname))
#
#     fetched_player = await player_repository.get_by_player_nickname(nickname)
#
#     assert fetched_player is not None
#     assert fetched_player.id == added_player.id
#     assert fetched_player.nickname == nickname
#
#
# async def test_get_player_by_nickname_not_found(player_repository: PlayerRepository):
#     """Тест: получение несуществующего игрока по никнейму вызывает PlayerNotFoundError."""
#     non_existent_nickname = Nickname("non_existent_nick")
#     with pytest.raises(PlayerNotFoundError):
#         await player_repository.get_by_player_nickname(non_existent_nickname)
#
#
# async def test_update_player_rating(player_repository: PlayerRepository, db_session: AsyncSession):
#     """Тест обновления рейтинга игрока."""
#     nickname = Nickname("test_update_rating")
#     player = await player_repository.create(PlayerCreationData(nickname=nickname))
#     original_rating = player.rating
#
#     new_rating = Rating(1600)
#     player.rating = new_rating # Обновляем экземпляр сущности
#
#     updated_player = await player_repository.update(player) # Сохраняем изменения через репозиторий
#
#     assert updated_player is not None
#     assert updated_player.id == player.id
#     assert updated_player.rating == new_rating
#     assert updated_player.rating != original_rating
#
#     # Проверяем в БД, что рейтинг действительно обновился
#     fetched_player = await player_repository.get_by_player_id(player.id)
#     assert fetched_player is not None
#     assert fetched_player.rating == new_rating
#
#
# async def test_update_player_nickname_fails_constraint(player_repository: PlayerRepository, db_session: AsyncSession):
#     """Тест: обновление никнейма не удается, если он уже занят другим игроком."""
#     nick1 = Nickname("update_nick_1")
#     nick2 = Nickname("update_nick_2")
#     player1 = await player_repository.create(PlayerCreationData(nickname=nick1))
#     await player_repository.create(PlayerCreationData(nickname=nick2)) # Добавляем второго игрока с другим ником
#
#     # Пытаемся обновить никнейм player1 на nick2, который уже занят
#     player1.nickname = nick2
#     with pytest.raises(PlayerAlreadyExistsError): # Ожидаем нарушение ограничения уникальности
#         await player_repository.update(player1)
#
#     # Проверяем, что никнейм player1 не изменился в БД (из-за отката транзакции в фикстуре db_session)
#     refetched_player1 = await player_repository.get_by_player_id(player1.id)
#     assert refetched_player1.nickname == nick1 # Никнейм должен остаться прежним
#
#
# async def test_delete_player_success(player_repository: PlayerRepository, db_session: AsyncSession):
#     """Тест успешного удаления существующего игрока."""
#     nickname = Nickname("test_delete_success")
#     player = await player_repository.create(PlayerCreationData(nickname=nickname))
#
#     await player_repository.delete(player.id)
#
#     # Проверяем, что игрок действительно удален (попытка получить его вызовет ошибку)
#     with pytest.raises(PlayerNotFoundError):
#         await player_repository.get_by_player_id(player.id)
#
#
# async def test_delete_player_not_found(player_repository: PlayerRepository):
#     """Тест: удаление несуществующего игрока вызывает PlayerNotFoundError."""
#     non_existent_id = PlayerId(value=99999999)
#     with pytest.raises(PlayerNotFoundError):
#         await player_repository.delete(non_existent_id)
