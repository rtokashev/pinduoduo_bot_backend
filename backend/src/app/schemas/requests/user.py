from typing import Union

from pydantic import BaseModel, Field


class NewUserRequestSchema(BaseModel):

    telegram_id: int = Field(..., description='Телеграмм(чат) айди пользователя')
    phone: Union[str, None] = Field(..., description='Телефон пользователя')
    username: str
    language_code: Union[str, None]

    class Config:
        orm_mode = True
