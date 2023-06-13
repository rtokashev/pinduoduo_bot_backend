import datetime

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer, String, Text, UniqueConstraint

from src.database.session import Base


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
    subscription_end_date = Column(Boolean, nullable=True, index=True)  # По хорошему надо индексировать
    created_at = Column(DateTime, default=datetime.datetime.now())


class JointPurchaseRequest(Base):

    __tablename__ = 'joint_purchase_request'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    chat_id = Column(BigInteger, nullable=False, unique=True)  # Индексировать ли?
    link = Column(String, nullable=False, unique=True)  # Определиться с ограничениями
    goods_id = Column(Integer, nullable=False, index=True)
    photo = Column(Text, nullable=False)  # Определиться что лучше для хранения(string или text)
    post_id = Column(Integer, nullable=False)
    post_url = Column(String, nullable=False)
    is_active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.now(), index=True)  #  Надо индексировать тоже
