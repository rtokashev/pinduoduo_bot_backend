from sqlalchemy import BigInteger, Column, ForeignKey, Integer, SmallInteger

from src.core.database.session import Base

__all__ = [
    'Limits',
]


class Limits(Base):
    __tablename__ = 'limits'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    telegram_id = Column(BigInteger, ForeignKey('users.telegram_id'), nullable=False, unique=True)
    free_requests_count = Column(SmallInteger, nullable=False, default=3)
    daily_requests_count = Column(SmallInteger, nullable=True)
