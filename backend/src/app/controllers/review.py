from app.models.review import Review
from core.controller.base import BaseController


class ReviewController(BaseController[Review]):
    """Слой бизнес логики для запросов по товарам."""
