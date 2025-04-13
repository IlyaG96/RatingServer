from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GameId:
    value: UUID
