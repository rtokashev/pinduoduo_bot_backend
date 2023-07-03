from sqlalchemy.sql.expression import select

from app.models.limits import Limits
from core.repository.base import BaseRepository


class UserLimitsRepository(BaseRepository[Limits]):
    """Слой непосредственной работы с БД."""

    async def get_user_limits(self, telegram_id: int) -> Limits:
        query = select(self.model).filter(*[self.model.telegram_id == telegram_id])
        return await self._one(query)
