from src.application.use_cases.base import ExceptionWithDetails


class DatabaseError(Exception, ExceptionWithDetails):
    def __init__(self, details: str) -> None:
        self._details = details

    @property
    def details(self) -> str:
        return self._details
