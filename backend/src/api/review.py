from fastapi import APIRouter, Depends, Response, status
from fastapi.exceptions import HTTPException

from app.controllers import factory as controllers_factory
from app.controllers.review import ReviewController
from app.schemas.requests.review import NewReviewSchema
from app.schemas.responses.review import ReviewResponseSchema

reviews_router = APIRouter()


@reviews_router.post(
    '',
    response_model=ReviewResponseSchema,
    summary='Создание отзыва на товар',
)
async def create_purchase_review(
    new_review: NewReviewSchema,
    review_controller: ReviewController = Depends(controllers_factory.get_purchase_review_controller),
):
    try:
        new_review = await review_controller.create(new_review.dict())
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err),
        )

    return Response(
        status_code=status.HTTP_201_CREATED if new_review else status.HTTP_200_OK,
    )
