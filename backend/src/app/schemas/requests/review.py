
from pydantic import BaseModel, Field


class NewReviewSchema(BaseModel):
    post_id: int = Field(..., description='Идентификатор на пост товара в канале')
    post_url: str = Field(..., description='Ссылка на пост товара в канале')
    goods_id: int = Field(..., description='Идентификатор товара(в платформе pinduoduo)')
