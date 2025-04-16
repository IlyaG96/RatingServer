from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, Protocol, TypeVar

from pydantic import BaseModel


class UseCase(ABC):
    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        pass


class ExceptionWithDetails(Protocol):
    @property
    def details(self) -> str: ...


ResultT = TypeVar("ResultT", bound=BaseModel)
ExceptionT = TypeVar("ExceptionT", bound=ExceptionWithDetails)


@dataclass(frozen=True)
class UseCaseResult(Generic[ResultT, ExceptionT]):
    data: ResultT | None
    error: ExceptionT | None
