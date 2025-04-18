from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, Literal, TypeVar, Union, final

from src.common.excpetion_with_details import ExceptionWithDetails

ResultT = TypeVar("ResultT")
ExceptionT = TypeVar("ExceptionT", bound=ExceptionWithDetails)


@final
@dataclass(frozen=True)
class Success(Generic[ResultT]):
    """Представляет успешный результат операции."""

    data: ResultT
    error: Literal[None] = None


@final
@dataclass(frozen=True)
class Failure(Generic[ExceptionT]):
    """Представляет результат операции с ошибкой."""

    error: ExceptionT
    data: Literal[None] = None


UseCaseResult = Union[Success[ResultT], Failure[ExceptionT]]


class UseCase(ABC):
    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> UseCaseResult:
        pass
