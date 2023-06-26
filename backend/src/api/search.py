from functools import partial
from typing import List, Union

from fastapi import APIRouter, Depends

from app.controllers import PurchaseController, UserController
from app.controllers import factory as controllers_factory
from app.schemas.requests.search import (
    CommonSearchSchema,
    PurchaseSearchSchema,
    UserSearchSchema,
    common_search_params,
)
from app.schemas.responses.purchase import PurchaseResponseSchema
from app.schemas.responses.user import UserResponseSchema

search_router = APIRouter()


@search_router.post(
    '',
    response_model=Union[List[UserResponseSchema], List[PurchaseResponseSchema]],
    summary='Поиск по заданным параметрам',
)
async def search(
    user_controller: UserController = Depends(controllers_factory.get_user_controller),
    joint_purchase_request_controller: PurchaseController = Depends(
        controllers_factory.get_purchase_controller,
    ),
    search_params: CommonSearchSchema = Depends(common_search_params),
):
    search_callbacks = {
        'user': partial(user_search, user_controller),
        'joint_purchase_request': partial(purchase_search, joint_purchase_request_controller),
    }
    if isinstance(search_params.value, UserSearchSchema):
        search_callback = search_callbacks['user']
    elif isinstance(search_params.value, PurchaseSearchSchema):
        search_callback = search_callbacks['joint_purchase_request']
    else:
        raise NotImplementedError('No more options for search yet')
    return await search_callback(search_params.value.dict(exclude_none=True), search_params.limit)


async def user_search(
    user_controller: UserController,
    attributes: dict,
    limit: int,
) -> List[UserResponseSchema]:
    found_results = await user_controller.search(attributes, limit)
    return [UserResponseSchema.from_orm(found_result) for found_result in found_results]


async def purchase_search(
    joint_purchase_request_controller: PurchaseController,
    attributes: dict,
    limit: int,
) -> List[PurchaseResponseSchema]:
    found_results = await joint_purchase_request_controller.search(attributes, limit)
    return [PurchaseResponseSchema.from_orm(found_result) for found_result in found_results]
