from fastapi import Depends

from app.controllers import (
    PurchaseController,
    ReferralController,
    ReviewController,
    UserController,
    UserLimitsController,
)
from app.repositories import (
    PurchaseRepository,
    ReferralRepository,
    ReviewRepository,
    UserLimitsRepository,
    UserRepository,
)
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


def get_user_limits_controller(db_session=Depends(get_async_db_session)):
    return UserLimitsController(
        repository=UserLimitsRepository(db_session),
    )


def get_purchase_review_controller(db_session=Depends(get_async_db_session)):
    return ReviewController(
        repository=ReviewRepository(db_session),
    )
