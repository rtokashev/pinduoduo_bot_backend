from sqlalchemy import update

from app.models.cargo import Cargo
from core.repository.base import BaseRepository


class CargoRepository(BaseRepository[Cargo]):
    """Слой непосредственной работы с БД."""

    async def update_paid_status_by_delivery_id(self, delivery_id: int):
        update_query = (
            update(self.model).
            where(self.model.id == delivery_id).
            values(
                paid=True,
            )
        )
        cursor = await self.db_session.execute(update_query)

        if not cursor.rowcount:
            raise Exception('No cargo delivery found by given delivery_id')

        await self.apply_changes()
