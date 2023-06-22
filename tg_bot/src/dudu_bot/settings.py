
from pydantic import BaseSettings
from pathlib import Path
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class Settings(BaseSettings):
    bot_token: str = '6059471641:AAEC8bKkfdaL_84SBqUDkOkXmSCSmqtpAU8'
    bot_admins: list = [767337244]
    # channel_chat_ids = [1809591303, 1985864035]
    channel_chat_ids = [-1001809591303, -1001985864035]
    # bot: Bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
    # storage: MemoryStorage = MemoryStorage()
    # dp: Dispatcher = Dispatcher(bot=bot, storage=storage)
    # base_dir: str = 'src'
    # abs_base_dir: str = str([p for p in Path(__file__).absolute().parents if p.name == base_dir][0])


settings = Settings()

BOT = Bot(token=settings.bot_token, parse_mode=types.ParseMode.HTML)
STORAGE = MemoryStorage()
DP = Dispatcher(BOT, storage=STORAGE)
