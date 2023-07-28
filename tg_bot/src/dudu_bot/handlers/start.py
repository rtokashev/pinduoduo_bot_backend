import httpx

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from dudu_bot.texts import main_texts
from dudu_bot.keyboards import (
    reg_rkm,
    main_rkm,
    admin_rkm,
)
from dudu_bot.settings import DP, BOT, settings
from dudu_bot.utils import APIClient
from dudu_bot.filters import IsNotBanned


@DP.message_handler(IsNotBanned(), CommandStart())
async def start(message: types.Message):
    request = APIClient()
    chat_id = message.chat.id
    param = {
        "limit": 1,
        "value": {
            "kind": "user",
            "telegram_id": chat_id
        }
    }
    try:
        response = await request.session.post(
            url=f'{settings.api_url}search',
            json=param
        )
    except httpx.ConnectError:
        response = None
    if response:
        await BOT.send_sticker(
            chat_id=chat_id,
            sticker=settings.welcome_sticker
        )
        user = response.json()
        if user:
            if chat_id in settings.bot_admins:
                await message.reply(
                    text=main_texts.welcome_txt,
                    reply=False,
                    reply_markup=admin_rkm
                )
            else:
                await message.reply(
                    text=main_texts.welcome_txt,
                    reply=False,
                    reply_markup=main_rkm
                )
        else:
            await message.reply(
                text=main_texts.welcome_txt,
                reply=False
            )
            await message.reply(
                text=main_texts.reg_txt,
                reply=False,
                reply_markup=reg_rkm
            )
    else:
        await message.reply(
            text=main_texts.error_txt,
            reply=False
        )

