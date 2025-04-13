from pydantic import BaseModel, Field

from src.domain.value_objects.nickname import Nickname
from src.domain.value_objects.player_id import PlayerId
from src.domain.value_objects.rating import Rating


class PlayerCreateRequest(BaseModel):
    nickname: Nickname = Field(..., description="Никнейм игрока")


class PlayerResponse(BaseModel):
    player_id: PlayerId
    nickname: Nickname
    rating: Rating

    class Config:
        from_attributes = True
