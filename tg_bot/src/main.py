from dudu_bot.handlers import DP
from aiogram import executor
from dudu_bot.settings import BOT, STORAGE
from dudu_bot.filters import setup_filters


async def on_shutdown(dp):
    await BOT.close()
    await STORAGE.close()


async def on_startup(dp):
    await setup_filters(dp)


if __name__ == '__main__':
    executor.start_polling(
        DP,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
