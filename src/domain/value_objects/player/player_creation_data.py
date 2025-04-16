from pydantic import BaseModel

from src.domain.value_objects.player.nickname import Nickname


class PlayerCreationData(BaseModel):
    nickname: Nickname
