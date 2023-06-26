import datetime

from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from src.core.database.session import Base

__all__ = [
    'Purchase',
    'Base',
]


class Purchase(Base):
    __tablename__ = 'joint_purchase_request'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    chat_id = Column(
        BigInteger, ForeignKey('users.telegram_id'), nullable=False,
    )  # Индексировать ли? Надо ли делать уникальным?
    link = Column(String, nullable=False, unique=True)  # Определиться с ограничениями
    goods_id = Column(Integer, nullable=False, index=True)
    photo = Column(Text, nullable=False)  # Определиться что лучше для хранения(string или text)
    post_id = Column(Integer, nullable=False)
    post_url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime, default=datetime.datetime.now, index=True,
    )  # Надо индексировать тоже?
    user = relationship('User', back_populates='joint_purchase_requests')
