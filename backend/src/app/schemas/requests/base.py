from enum import Enum


class Kind(Enum):
    USER = 'user'
    PURCHASE = 'purchase'
    REVIEW = 'review'


class ActionType(Enum):
    UPDATE = 'update'
    DELETE = 'delete'
