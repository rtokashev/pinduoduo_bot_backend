from pydantic import BaseSettings
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class Settings(BaseSettings):
    bot_token: str = '6059471641:AAEC8bKkfdaL_84SBqUDkOkXmSCSmqtpAU8'
    bot_admins: list = [767337244]
    channel_chat_ids = [-1001809591303, -1001985864035]
    welcome_sticker: str = 'CAACAgIAAxkBAAEJZ0xkkIY8Corsu4W_mu9jXAjHaBFM_wACAhYAAg0naUpXB81IWRo4wy8E'
    goods_url: str = 'https://mobile.yangkeduo.com/goods1.html?goods_id={}'
    post_url: str = 'https://t.me/c/1809591303/{}'
    api_url: str = 'http://127.0.0.1:8000/'


settings = Settings()

BOT = Bot(token=settings.bot_token, parse_mode=types.ParseMode.HTML)
STORAGE = MemoryStorage()
DP = Dispatcher(BOT, storage=STORAGE)
