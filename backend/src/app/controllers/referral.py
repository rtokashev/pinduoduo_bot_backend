from app.models.referral import Referral
from core.controller.base import BaseController


class ReferralController(BaseController[Referral]):
    """Слой бизнес логики для запросов по рефералкам."""
