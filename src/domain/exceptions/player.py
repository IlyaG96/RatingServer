from src.common.excpetion_with_details import ExceptionWithDetails


class PlayerNotFoundError(Exception, ExceptionWithDetails):
    def __init__(self, details: str) -> None:
        self._details = details

    @property
    def details(self) -> str:
        return self._details


class PlayerAlreadyExistsError(Exception, ExceptionWithDetails):
    def __init__(self, details: str) -> None:
        self._details = details

    @property
    def details(self) -> str:
        return self._details
