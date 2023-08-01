from typing import Union

from pydantic import BaseModel, Field


class NewCargoDeliverySchema(BaseModel):
    chat_id: int = Field(..., description='chat_id пользователя')
    weight: float = Field(..., description='Вес посылки')
    price: int = Field(..., description='Цена(по весу) посылки')
    paid: Union[bool, None] = Field(..., description='Статус оплаты посылки')
