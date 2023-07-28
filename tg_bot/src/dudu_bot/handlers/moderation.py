from aiogram import types
from dudu_bot.settings import DP
from dudu_bot.utils import check_text


@DP.message_handler()
async def moderate_text(message: types.Message):
    text = message.text
    if check_text(text=text):
        await message.delete()
