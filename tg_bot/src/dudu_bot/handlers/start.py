from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from dudu_bot.texts import main_texts
from dudu_bot.keyboards import (
    reg_rkm,
    main_rkm,
    about_bot_ikm,
)
from dudu_bot.settings import DP, BOT, settings


@DP.message_handler(CommandStart())
async def start(message: types.Message):
    chat_id = message.chat.id
    is_user = False #TODO
    await BOT.send_sticker(
        chat_id=chat_id,
        sticker=settings.welcome_sticker
    )
    if is_user:
        await message.reply(
            text=main_texts.welcome_txt,
            reply=False,
            reply_markup=main_rkm
        )
    else:
        await message.reply(
            text=main_texts.welcome_txt,
            reply=False,
            reply_markup=about_bot_ikm
        )
        await message.reply(
            text=main_texts.reg_txt,
            reply=False,
            reply_markup=reg_rkm
        )