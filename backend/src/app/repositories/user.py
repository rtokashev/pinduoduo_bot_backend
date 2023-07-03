from sqlalchemy.sql.expression import update

from app.models.user import User
from core.repository.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Слой непосредственной работы с БД."""

    async def set_banned_status(self, telegram_id: int, is_banned: bool):
        update_query = (
            update(self.model).
            where(self.model.telegram_id == telegram_id).
            values(
                is_subscriber=False,
                subscription_end_date=None,
                is_banned=is_banned
            )
        )
        cursor = await self.db_session.execute(update_query)

        if not cursor.rowcount:
            raise Exception('No user found by given telegram_id')

        await self.apply_changes()
