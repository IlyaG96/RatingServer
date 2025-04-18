from fastapi import Request
from starlette.responses import Response, JSONResponse

from src.infrastructure.exceptions.database import DatabaseError

def database_exception_handler(request: Request, exc: DatabaseError) -> Response:
    return JSONResponse(
        status_code=503,
        content={"message": f"Service unavailable: {exc.details}"}
    )