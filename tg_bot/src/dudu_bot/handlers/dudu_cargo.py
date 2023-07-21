import httpx

from aiogram import types
from dudu_bot.texts import main_texts
from dudu_bot.settings import DP, settings
from dudu_bot.filters import IsNotBanned, IsChannelsSubscriber
from dudu_bot.keyboards import cargo_code_ikm
from dudu_bot.utils import APIClient


@DP.message_handler(
    IsNotBanned(),
    IsChannelsSubscriber(),
    regexp=fr'{main_texts.dudu_cargo_btn}',
)
async def dudu_cargo_info(message: types.Message):
    await message.answer(
        text=main_texts.cargo_info_txt,
        reply_markup=cargo_code_ikm,
    )


@DP.callback_query_handler(text_contains="cargo_code")
async def cargo_code(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    request = APIClient()
    chat_id = call.message.chat.id
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
        await call.message.answer(
            text=main_texts.cargo_address_txt.format(
                chat_id=call.message.chat.id,
                phone=response.json()[0].get('phone')
            ),
            disable_web_page_preview=True,
        )
    else:
        await call.message.reply(
            text=main_texts.error_txt,
            reply=False
        )
