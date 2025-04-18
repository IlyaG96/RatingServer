from typing import Protocol


class ExceptionWithDetails(Protocol):
    @property
    def details(self) -> str: ...
