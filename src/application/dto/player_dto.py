from pydantic import BaseModel, Field


class CreatePlayerDTO(BaseModel):
    nickname: str = Field(...)


class GetPlayerDTO(BaseModel):
    nickname: str = Field(...)
