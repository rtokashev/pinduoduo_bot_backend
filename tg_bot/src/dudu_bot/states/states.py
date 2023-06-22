from aiogram.dispatcher.filters.state import StatesGroup, State


class UserRegister(StatesGroup):
    Telephone = State()
    Channel = State()
