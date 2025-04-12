class Player:
    def __init__(self, player_id: str, rating: int, nickname: str):
        self._player_id = player_id
        self._rating = rating
        self._nickname = nickname

    def update_rating(self, new_rating: int) -> None:
        """Обновление рейтинга игрока."""
        self._rating = new_rating

    async def persist(self, repository) -> None:
        """Сохранение через репозиторий."""
        await repository.save(self)
