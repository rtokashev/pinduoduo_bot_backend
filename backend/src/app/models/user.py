import datetime

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from core.database.session import Base

__all__ = [
    'User',
]


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('telegram_id', 'phone'),
    )

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    telegram_id = Column(BigInteger, nullable=False, unique=True)  # Индексировать ли?
    phone = Column(String, nullable=True, unique=True)
    username = Column(String, nullable=False)  # Индексировать ли?
    language_code = Column(String, nullable=True, default='RU')
    is_banned = Column(Boolean, default=False, nullable=True)
    is_subscriber = Column(Boolean, default=False, nullable=True)
    subscription_end_date = Column(
        DateTime, nullable=True, index=True,
    )  # По хорошему надо индексировать
    created_at = Column(DateTime, default=datetime.datetime.now)
    joint_purchase_requests = relationship('Purchase', back_populates='user')
