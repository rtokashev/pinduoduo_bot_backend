from fastapi import Depends

from app.controllers import PurchaseController, ReferralController, UserController
from app.repositories import PurchaseRepository, ReferralRepository, UserRepository
from core.dependencies.database import get_async_db_session


def get_purchase_controller(db_session=Depends(get_async_db_session)):
    return PurchaseController(
        repository=PurchaseRepository(db_session),
    )


def get_referral_controller(db_session=Depends(get_async_db_session)):
    return ReferralController(
        repository=ReferralRepository(db_session),
    )


def get_user_controller(db_session=Depends(get_async_db_session)):
    return UserController(
        repository=UserRepository(db_session),
    )
