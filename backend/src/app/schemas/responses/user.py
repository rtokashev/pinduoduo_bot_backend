import datetime
from typing import Union

from pydantic import BaseModel, Field


class UserResponseSchema(BaseModel):
    telegram_id: int = Field(..., description='Телеграмм(чат) айди пользователя')
    phone: Union[str, None] = Field(..., description='Телефон пользователя')
    username: str
    language_code: Union[str, None]
    is_banned: Union[bool, None] = Field(..., description='Признак забаненного пользователя')
    is_subscriber: Union[bool, None]
    subscription_end_date: Union[datetime.datetime, None]
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class UserBannedResponse(BaseModel):
    telegram_id: int = Field(..., description='Телеграмм(чат) айди пользователя')
    is_banned: bool = Field(..., description='Признак забаненного пользователя')
