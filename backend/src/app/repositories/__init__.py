from app.repositories.cargo import CargoRepository
from app.repositories.limits import UserLimitsRepository
from app.repositories.purchase import PurchaseRepository
from app.repositories.referral import ReferralRepository
from app.repositories.review import ReviewRepository
from app.repositories.user import UserRepository

__all__ = [
    'CargoRepository',
    'PurchaseRepository',
    'ReferralRepository',
    'ReviewRepository',
    'UserLimitsRepository',
    'UserRepository',
]
