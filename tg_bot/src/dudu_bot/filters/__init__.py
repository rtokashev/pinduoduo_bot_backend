from aiogram import Dispatcher
from .filters import (
    IsNotBanned,
    IsChannelsSubscriber
)


async def setup_filters(dp: Dispatcher):
    dp.filters_factory.bind(IsNotBanned)
    dp.filters_factory.bind(IsChannelsSubscriber)
