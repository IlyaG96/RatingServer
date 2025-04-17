from pydantic import BaseModel, Field


class CreatePlayerDTO(BaseModel):
    nickname: str = Field(...)


class GetPlayerDTO(BaseModel):
    nickname: str = Field(...)


class PlayerResponseDTO(BaseModel):
    player_id: int = Field(..., description="ID игрока")
    nickname: str = Field(..., description="Никнейм игрока")
    rating: int = Field(..., description="Рейтинг игрока")
