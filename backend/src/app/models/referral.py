import datetime

from sqlalchemy import BigInteger, Column, DateTime, Integer

from core.database.session import Base

__all__ = [
    'Referral',
]


class Referral(Base):

    __tablename__ = 'referrals'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True, nullable=False)
    referred_id = Column(BigInteger)
    created_at = Column(
        DateTime, default=datetime.datetime.now, index=True,
    )  # Надо индексировать тоже?
