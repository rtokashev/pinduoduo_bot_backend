from fastapi import APIRouter, Depends, Path, Response, status
from fastapi.exceptions import HTTPException

from app.controllers import factory as controllers_factory
from app.controllers.cargo import CargoController
from app.schemas.requests.cargo import NewCargoDeliverySchema
from app.schemas.responses.cargo import CargoResponseSchema

cargo_router = APIRouter()


@cargo_router.post(
    '',
    response_model=CargoResponseSchema,
    summary='Создание записи по новой посылке',
)
async def create_cargo_delivery_record(
    new_cargo_delivery: NewCargoDeliverySchema,
    cargo_controller: CargoController = Depends(controllers_factory.get_cargo_controller),
):
    try:
        new_cargo_delivery = await cargo_controller.create(new_cargo_delivery.dict())
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err),
        )
    return CargoResponseSchema.from_orm(new_cargo_delivery)


@cargo_router.put(
    path='/{delivery_id}/paid',
    status_code=status.HTTP_200_OK,
    description='Смена статуса оплаты',
)
async def set_cargo_delivery_paid(
    cargo_controller: CargoController = Depends(controllers_factory.get_cargo_controller),
    delivery_id: int = Path(),
):
    try:
        await cargo_controller.update_paid_status_by_delivery_id(delivery_id)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err),
        )
    return Response(status_code=status.HTTP_200_OK)
