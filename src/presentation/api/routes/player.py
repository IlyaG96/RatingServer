from fastapi import APIRouter, HTTPException, status

from src.application.dto.player_dto import CreatePlayerDTO, GetPlayerDTO
from src.application.use_cases.base import Failure, Success
from src.application.use_cases.create_player import CreatePlayer
from src.application.use_cases.get_player import GetPlayer
from src.infrastructure.di.di_container import dependency_container
from src.presentation.api.schemas.player import CreatePlayerRequest, PlayerResponse

router = APIRouter(prefix="/players", tags=["Players"])


@router.post("/", status_code=status.HTTP_201_CREATED, summary="Создать нового игрока")
async def create_player(request: CreatePlayerRequest) -> None:
    """
    Чистая команда: Соответствует CQRS (разделение команд и запросов): создание — это команда, она меняет состояние,
    но не возвращает данные.
    """
    use_case = CreatePlayer(dependency_container.player_repository)
    result = await use_case.execute(CreatePlayerDTO(nickname=request.nickname))

    if isinstance(result, Failure):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result.error.details)
    if isinstance(result, Success):
        return
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/{player_nickname}", status_code=status.HTTP_200_OK, summary="Получить игрока по никнейму")
async def get_player_by_nickname(player_nickname: str) -> PlayerResponse:
    use_case = GetPlayer(dependency_container.player_repository)
    result = await use_case.execute(GetPlayerDTO(nickname=player_nickname))
    if isinstance(result, Success):
        return PlayerResponse(player_id=result.data.player_id, nickname=result.data.nickname, rating=result.data.rating)
    elif isinstance(result, Failure):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result.error.details)
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
