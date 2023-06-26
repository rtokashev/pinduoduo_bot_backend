from app.models.purchase import Purchase
from core.controller.base import BaseController


class PurchaseController(BaseController[Purchase]):
    """Слой бизнес логики для запросов по товарам."""
