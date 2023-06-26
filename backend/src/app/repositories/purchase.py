from app.models.purchase import Purchase
from core.repository.base import BaseRepository


class PurchaseRepository(BaseRepository[Purchase]):
    """Слой непосредственной работы с БД."""
