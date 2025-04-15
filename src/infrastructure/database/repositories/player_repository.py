from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.application.dto.player_dto import PlayerCreateDTO
from src.domain.entities.player import Player
from src.domain.exceptions.player import PlayerNotFoundError
from src.domain.repositories.player_repository import PlayerRepositoryInterface
from src.domain.value_objects.nickname import Nickname
from src.domain.value_objects.player_id import PlayerId
from src.domain.value_objects.rating import Rating
from src.infrastructure.database.async_database import SQLAlchemyDataBase
from src.infrastructure.database.models.player import PlayerModel


class PlayerRepository(PlayerRepositoryInterface):
    def __init__(self, database: SQLAlchemyDataBase) -> None:
        self.database = database

    async def get_by_player_id(self, player_id: PlayerId) -> Player:
        """

        :param player_id:
        :return: Player entity
        :raises PlayerNotFoundError: when player does not exist.
        """
        query = select(PlayerModel).where(PlayerModel.player_id == player_id)

        async with self.database.get_session() as session:
            result = await session.execute(query)
            player = result.scalar_one_or_none()
        if player is None:
            raise PlayerNotFoundError
        return Player(
            player_id=PlayerId(player.player_id),
            nickname=Nickname(player.nickname),
            rating=Rating(player.rating)
        )

    async def persist(self, player: Player) -> None:
        pass

    async def create(self, player: PlayerCreateDTO) -> None:

        player_model = PlayerModel(nickname=player.nickname)
        try:
            async with self.database.get_session() as session:
                session.add(player_model)
                await session.commit()
        except IntegrityError:
            raise
