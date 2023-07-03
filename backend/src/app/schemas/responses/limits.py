from typing import Union

from pydantic import BaseModel, Field


class UserLimitsResponseSchema(BaseModel):
    telegram_id: int = Field(..., description='Телеграмм(чат) айди пользователя')
    # has_available_limits: bool = Field(
    #     ..., description='Признак, что пользователь не исчерпал лимит запросов'
    # )
    free_requests_count: int = Field(..., description='Кол-во доступных бесплатных запросов')
    total_requests_count: Union[int, None] = Field(
        ..., description='Общее кол-во доступных запросов(при активной подписке)'
    )
    daily_requests_count: Union[int, None] = Field(
        ..., description='Кол-во доступных запросов в день(при активной подписке)'
    )
    available_requests_count: Union[int, None] = Field(
        ..., description='Общее кол-во использованных запросов(при активной подписке)'
    )

    class Config:
        orm_mode = True
