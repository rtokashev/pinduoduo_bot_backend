from app.models.review import Review
from core.repository.base import BaseRepository


class ReviewRepository(BaseRepository[Review]):
    """Слой непосредственной работы с БД."""
