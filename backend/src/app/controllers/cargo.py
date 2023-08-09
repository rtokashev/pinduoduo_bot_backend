from app.models.cargo import Cargo
from app.repositories.cargo import CargoRepository
from core.controller.base import BaseController


class CargoController(BaseController[Cargo]):
    """Слой бизнес логики для запросов по пользователям."""

    def __init__(self, repository: CargoRepository):
        super().__init__(repository)
        self.user_repository = repository

    async def update_paid_status_by_delivery_id(self, delivery_id: int):
        await self.user_repository.update_paid_status_by_delivery_id(delivery_id)
