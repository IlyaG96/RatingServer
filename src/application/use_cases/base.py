from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

from src.common.excpetion_with_details import ExceptionWithDetails


class UseCase(ABC):
    @abstractmethod
    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        pass


ResultT = TypeVar("ResultT", bound=BaseModel)
ExceptionT = TypeVar("ExceptionT", bound=ExceptionWithDetails)


@dataclass(frozen=True)
class UseCaseResult(Generic[ResultT, ExceptionT]):
    data: ResultT | None
    error: ExceptionT | None
