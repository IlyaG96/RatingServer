from pydantic import BaseModel, Field


class CreatePlayerRequest(BaseModel):
    nickname: str = Field(..., description="Никнейм игрока")


class GetPlayerByNicknameRequest(BaseModel):
    nickname: str = Field(..., description="Никнейм игрока")


class PlayerResponse(BaseModel):
    player_id: int = Field(..., description="ID игрока")
    nickname: str = Field(..., description="Никнейм игрока")
    rating: int = Field(..., description="Рейтинг игрока")

    class ConfigDict:
        from_attributes = True
