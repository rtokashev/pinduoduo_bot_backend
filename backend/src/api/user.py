from typing import List

from fastapi import APIRouter, Depends, Path, Query, Response, status
from fastapi.exceptions import HTTPException

from app.controllers import factory as controllers_factory
from app.controllers.user import UserController
from app.schemas.requests.user import NewUserRequestSchema
from app.schemas.responses.user import UserBannedResponse, UserResponseSchema

users_router = APIRouter()


@users_router.get(
    '',
    response_model=List[UserResponseSchema],
    status_code=status.HTTP_200_OK,
    summary='Получение всех пользователей(вне зависимости от статуса(пока что))',
)
async def get_all_users(
    user_controller: UserController = Depends(controllers_factory.get_user_controller),
):
    return await user_controller.get_all()


@users_router.post(
    '',
    response_model=UserResponseSchema,
    summary='Создание нового пользователя(без подписки)',
)
async def create_user(
    new_user: NewUserRequestSchema,
    user_controller: UserController = Depends(controllers_factory.get_user_controller),
):
    try:
        new_user = await user_controller.create(new_user.dict())
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err),
        )

    return Response(
        status_code=status.HTTP_201_CREATED if new_user else status.HTTP_200_OK,
    )


@users_router.get(
    path='/{telegram_id}/status',
    status_code=status.HTTP_200_OK,
    description='Смена статуса пользователя(бан или наоборот)',
)
async def set_user_banned(
    user_controller: UserController = Depends(controllers_factory.get_user_controller),
    telegram_id: int = Path(),
    is_banned: bool = Query(),
) -> UserBannedResponse:
    try:
        await user_controller.set_banned_status(telegram_id, is_banned)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err),
        )
    return UserBannedResponse(
        telegram_id=telegram_id,
        is_banned=is_banned,
    )
