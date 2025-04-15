import uvicorn
from fastapi import FastAPI

from src.application.api.routes.player import router as player_router

app = FastAPI()
app.include_router(router=player_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
