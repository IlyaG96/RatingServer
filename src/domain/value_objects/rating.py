from typing import Annotated

from pydantic import conint

Rating = Annotated[int, conint(ge=0)]
