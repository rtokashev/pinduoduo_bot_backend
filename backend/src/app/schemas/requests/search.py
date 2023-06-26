from typing import Literal, Union

from pydantic import BaseModel, Extra, Field

from app.schemas.requests.base import Kind


class ConfiguredBaseModel(BaseModel):

    class Config:
        extra = Extra.forbid
        fields = {
            'kind': {
                'exclude': True,
            },
        }


class UserSearchSchema(ConfiguredBaseModel):
    kind: Literal[Kind.USER.value]
    telegram_id: Union[int, None]
    phone: Union[str, None]
    username: Union[str, None]
    is_banned: Union[bool, None]



class PurchaseSearchSchema(ConfiguredBaseModel):
    kind: Literal[Kind.PURCHASE.value]
    chat_id: Union[int, None]
    goods_id: Union[str, None]


class CommonSearchSchema(BaseModel):
    limit: int = Field(default=1, gt=0, lt=10)
    value: Union[UserSearchSchema, PurchaseSearchSchema] = Field(..., discriminator='kind')  # noqa: E501


def common_search_params(payload: CommonSearchSchema):
    return payload
