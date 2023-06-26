from app.models.user import User
from core.repository.base import BaseRepository


class ReferralRepository(BaseRepository[User]):
    """Слой непосредственной работы с БД."""
