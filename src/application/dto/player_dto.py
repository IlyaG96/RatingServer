from pydantic import BaseModel, Field


class PlayerCreateDTO(BaseModel):
    nickname: str = Field(..., min_length=3, max_length=255)
