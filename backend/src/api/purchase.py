"""
Пока делать обшие эндпоинты под дублирующиеся эндпоинты не стоит.

Так как возможно будут добавляться сложные условия фильтраций и тд.
"""
from typing import List

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app.controllers import factory as controllers_factory
from app.controllers.limits import UserLimitsController
from app.controllers.purchase import PurchaseController
from app.schemas.requests.purchase import NewPurchaseSchema
from app.schemas.responses.purchase import PurchaseResponseSchema

purchases_router = APIRouter()


@purchases_router.get(
    '',
    response_model=List[PurchaseResponseSchema],
    status_code=status.HTTP_200_OK,
    summary='Получение всех заявок(вне зависимости от статуса(пока что))',
)
async def get_all_purchases(
    purchase_controller: PurchaseController = Depends(controllers_factory.get_purchase_controller),
):
    return await purchase_controller.get_all()


@purchases_router.post(
    '',
    response_model=PurchaseResponseSchema,
    summary='Создание новой заявки на совместную покупку',
)
async def create_purchase(
    new_purchase: NewPurchaseSchema,
    purchase_controller: PurchaseController = Depends(controllers_factory.get_purchase_controller),
    user_limits_controller: UserLimitsController = Depends(controllers_factory.get_user_limits_controller)
):
    user_has_available_limits = await user_limits_controller.user_has_available_limits(new_purchase.chat_id)
    if not user_has_available_limits:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='User has reached limits of requests(daily or free)',
        )
    try:
        new_purchase = await purchase_controller.create(new_purchase.dict())
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err),
        )
    await user_limits_controller.reduce_user_limits(new_purchase.chat_id)
    return JSONResponse(
        content=jsonable_encoder(PurchaseResponseSchema.from_orm(new_purchase)),
        status_code=status.HTTP_201_CREATED if new_purchase else status.HTTP_200_OK,
    )
