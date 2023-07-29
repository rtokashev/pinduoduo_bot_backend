import datetime

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, Boolean, Float

from core.database.session import Base

__all__ = [
    'Cargo',
    'Base',
]


class Cargo(Base):
    __tablename__ = 'cargo'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    chat_id = Column(
        BigInteger, ForeignKey('users.telegram_id'), nullable=False,
    )
    weight = Column(Float, nullable=False)
    price = Column(Integer, nullable=False)
    paid = Column(Boolean, nullable=True)
    created_at = Column(
        DateTime, default=datetime.datetime.now, index=True,
    )
