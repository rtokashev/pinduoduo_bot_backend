from enum import Enum

from pydantic import BaseModel, Extra


class Kind(Enum):
    USER = 'user'
    PURCHASE = 'purchase'
    REVIEW = 'review'


class ActionType(Enum):
    UPDATE = 'update'
    DELETE = 'delete'
