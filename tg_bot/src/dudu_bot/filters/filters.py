import httpx

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from dudu_bot.settings import settings, BOT
from dudu_bot.utils import APIClient
from dudu_bot.keyboards import filter_channel_link_ikm
from dudu_bot.texts import main_texts


class IsChannelsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        check = list()
        for channel_chat_id in settings.channel_chat_ids:
            sub = await BOT.get_chat_member(chat_id=channel_chat_id, user_id=message.chat.id)
            if sub.status != types.ChatMemberStatus.LEFT:
                check.append(True)
            else:
                check.append(False)
        if all(check):
            return True
        else:
            await BOT.send_message(
                chat_id=message.chat.id,
                text=main_texts.channel_sub_txt,
                reply_markup=filter_channel_link_ikm
            )
            return False


class IsNotBanned(BoundFilter):
    async def check(self, message: types.Message):
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
            is_banned = response.json()[0].get('is_banned', False)
            if is_banned:
                await message.answer(
                    text=main_texts.is_banned_txt,
                    reply_markup=types.ReplyKeyboardRemove()
                )
                return False
            else:
                return True
        else:
            await message.reply(
                text=main_texts.error_txt,
                reply=False
            )
