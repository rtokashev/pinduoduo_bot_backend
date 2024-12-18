import datetime

from pydantic import BaseModel, Field


class PurchaseResponseSchema(BaseModel):
    chat_id: int = Field(..., description='Телеграмм(чат) айди пользователя')
    link: str = Field(..., description='Ссылка на товар')
    goods_id: int = Field(..., description='Идентификатор товара(в платформе pinduoduo)')
    photo: str = Field(..., description='Фотка товара в base64 формате')
    post_id: int = Field(..., description='Идентификатор на пост товара в канале')
    post_url: str = Field(..., description='Ссылка на пост товара в канале')
    is_active: bool = Field(..., description='Активен ли запрос на товар(пост и тд)')
    created_at: datetime.datetime

    class Config:
        orm_mode = True
