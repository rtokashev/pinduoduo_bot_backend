from enum import Enum

from pydantic import BaseModel, Extra


class Kind(Enum):
    USER = 'user'
    PURCHASE = 'purchase'


class ActionType(Enum):
    UPDATE = 'update'
    DELETE = 'delete'


class ConfiguredBaseModel(BaseModel):

    class Config:
        extra = Extra.forbid
        fields = {
            'kind': {
                'exclude': True,
            },
        }
