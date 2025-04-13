from typing import Annotated

from pydantic import constr

Nickname = Annotated[
    str, constr(min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")
]
