import uvicorn
from fastapi import FastAPI

from src.infrastructure.exceptions.database import DatabaseError
from src.presentation.api.middleaware.db_exception_handler import database_exception_handler
from src.presentation.api.routes.player import router as player_router

app = FastAPI()

app.exception_handler(DatabaseError)(database_exception_handler)

app.include_router(router=player_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
