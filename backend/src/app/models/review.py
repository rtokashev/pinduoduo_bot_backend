import datetime

from sqlalchemy import BigInteger, Column, DateTime, Integer, String

from core.database.session import Base

__all__ = [
    'Review',
    'Base',
]


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    post_id = Column(Integer, nullable=False)
    post_url = Column(String, nullable=False)
    goods_id = Column(BigInteger, nullable=False, index=True)
    goods_url = Column(String(length=2048), nullable=True)
    created_at = Column(
        DateTime, default=datetime.datetime.now, index=True,
    )
