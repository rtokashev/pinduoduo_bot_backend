from app.models.limits import Limits
from app.repositories.limits import UserLimitsRepository
from core.controller.base import BaseController


class UserLimitsController(BaseController[UserLimitsRepository]):
    """Слой бизнес логики для запросов по пользователям."""

    def __init__(self, repository: UserLimitsRepository):
        super().__init__(repository)
        self.user_limits_repository = repository

    async def get_user_limits(self, telegram_id: int):
        return await self.user_limits_repository.get_user_limits(telegram_id)

    async def user_has_available_limits(self, telegram_id) -> bool:
        user_limits = await self.get_user_limits(telegram_id)
        return any([user_limits.free_requests_count, user_limits.daily_requests_count])

    async def reduce_user_limits(self, telegram_id: int, used_limit: int = 1):
        user_limits: Limits = await self.user_limits_repository.get_user_limits(telegram_id)
        if user_limits.free_requests_count:
            user_limits.free_requests_count = user_limits.free_requests_count - used_limit
        elif user_limits.daily_requests_count:
            user_limits.daily_requests_count = user_limits.daily_requests_count - used_limit
        await self.user_limits_repository.apply_changes()
