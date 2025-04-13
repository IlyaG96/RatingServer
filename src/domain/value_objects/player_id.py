from dataclasses import dataclass


@dataclass(frozen=True)
class PlayerId:
    value: int
