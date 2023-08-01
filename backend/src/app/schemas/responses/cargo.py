import datetime

from pydantic import BaseModel, Field


class CargoResponseSchema(BaseModel):
    id: int = Field(..., description='ID посылки cargo')
    chat_id: int = Field(..., description='chat_id пользователя')
    weight: float = Field(..., description='Вес посылки')
    price: int = Field(..., description='Цена(по весу) посылки')
    paid: bool = Field(..., description='Статус оплаты посылки')
    created_at: datetime.datetime

    class Config:
        orm_mode = True
