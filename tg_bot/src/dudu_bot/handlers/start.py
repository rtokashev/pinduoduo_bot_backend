from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from dudu_bot.texts import main_texts
from dudu_bot.keyboards import (
    reg_rkm,
    main_rkm,
    about_bot_ikm,
)
from dudu_bot.settings import settings, DP, BOT


@DP.message_handler(CommandStart())
async def start(message: types.Message):
    chat_id = message.from_user.id
    is_user = False #TODO
    await BOT.send_sticker(
        chat_id=chat_id,
        sticker='CAACAgIAAxkBAAEJZ0xkkIY8Corsu4W_mu9jXAjHaBFM_wACAhYAAg0naUpXB81IWRo4wy8E'
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