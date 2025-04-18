from src.common.excpetion_with_details import ExceptionWithDetails


class DatabaseError(Exception, ExceptionWithDetails):
    def __init__(self, details: str) -> None:
        self._details = details

    @property
    def details(self) -> str:
        return self._details
