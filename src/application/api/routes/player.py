from fastapi import APIRouter, status

from src.application.api.schemas.player import PlayerCreateRequest
from src.application.dto.player_dto import PlayerCreateDTO
from src.application.use_cases.create_player import CreatePlayerUseCase
from src.infrastructure.database.repositories.player_repository import PlayerRepositorySQLAlchemy

router = APIRouter(prefix="/players", tags=["Players"])


@router.post("/", status_code=status.HTTP_201_CREATED, summary="Создать нового игрока")
async def create_player(request: PlayerCreateRequest) -> None:
    """
    Чистая команда: Соответствует CQRS (разделение команд и запросов): создание — это команда, она меняет состояние,
    но не возвращает данные.
    """
    await CreatePlayerUseCase().execute(PlayerCreateDTO(nickname=request.nickname))
