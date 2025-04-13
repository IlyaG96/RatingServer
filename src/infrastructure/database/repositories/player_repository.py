from sqlalchemy.exc import IntegrityError
from src.application.dto.player_dto import PlayerCreateDTO
from src.domain.entities.player import Player
from src.domain.repositories.player_repository import PlayerRepository
from src.domain.value_objects.nickname import Nickname
from src.domain.value_objects.player_id import PlayerId
from src.domain.value_objects.rating import Rating
from src.infrastructure.database.async_database import SQLAlchemyDataBase
from src.infrastructure.database.models.player import PlayerModel


class PlayerRepositorySQLAlchemy(PlayerRepository):

    def __init__(self, base: SQLAlchemyDataBase) -> None:
        self.base = base

    async def get_by_nickname(self, player_id: PlayerId) -> Player:
        return Player(player_id=PlayerId(1), nickname=Nickname("pppp"), rating=Rating(1111))

    async def persist(self, player: Player) -> None:
        pass

    async def create(self, player: PlayerCreateDTO) -> None:
        player_model = PlayerModel(nickname=player.nickname, )
        try:
            async with self.base.get_session() as session:
                session.add(player_model)
                await session.commit()
        except IntegrityError:
            raise
