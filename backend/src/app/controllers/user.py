from app.models.user import User
from app.repositories.user import UserRepository
from core.controller.base import BaseController


class UserController(BaseController[User]):
    """Слой бизнес логики для запросов по пользователям."""

    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        self.user_repository = repository

    async def set_banned_status(self, telegram_id: int, is_banned: bool):
        await self.user_repository.set_banned_status(telegram_id, is_banned)
