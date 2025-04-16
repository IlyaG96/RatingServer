from fastapi import APIRouter, HTTPException, status

from src.application.dto.player_dto import CreatePlayerDTO, GetPlayerDTO
from src.application.use_cases.create_player import CreatePlayer
from src.application.use_cases.get_player import GetPlayer
from src.di_container import dependency_container
from src.infrastructure.api.schemas.player import CreatePlayerRequest, PlayerResponse
from src.infrastructure.exceptions.database import DatabaseError

router = APIRouter(prefix="/players", tags=["Players"])


@router.post("/", status_code=status.HTTP_201_CREATED, summary="Создать нового игрока")
async def create_player(request: CreatePlayerRequest) -> None:
    """
    Чистая команда: Соответствует CQRS (разделение команд и запросов): создание — это команда, она меняет состояние,
    но не возвращает данные.
    """
    await CreatePlayer(dependency_container.player_repository).execute(CreatePlayerDTO(nickname=request.nickname))


@router.get("/{player_nickname}", status_code=status.HTTP_200_OK, summary="Получить игрока по никнейму")
async def get_player_by_nickname(player_nickname: str) -> PlayerResponse | None:
    try:
        use_case = GetPlayer(dependency_container.player_repository)
        result = await use_case.execute(GetPlayerDTO(nickname=player_nickname))
        if result.error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result.error.details)

        return result.result
    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=e.details,
        ) from e
