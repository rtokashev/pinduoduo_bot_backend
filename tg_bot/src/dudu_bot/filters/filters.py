from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from dudu_bot.settings import settings, BOT


class IsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        check = list()
        for channel_chat_id in settings.channel_chat_ids:
            sub = await BOT.get_chat_member(chat_id=channel_chat_id, user_id=message.from_user.id)
            if sub.status != types.ChatMemberStatus.LEFT:
                check.append(True)
            else:
                check.append(False)
        if all(check):
            return True
        else:
            return False
