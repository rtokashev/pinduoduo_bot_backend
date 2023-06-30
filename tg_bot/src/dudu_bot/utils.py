import re
import httpx
import aiohttp

from urllib.parse import urlparse, parse_qs
from dudu_bot.settings import settings, BOT
from aiogram import types


async def check_goods_url(url: str) -> bool:
    pattern = re.compile(r'(?=.*_oak_share_url)(?=.*goods_id)')
    if re.search(pattern, url):
        return True
    else:
        return False


async def get_goods_id_goods_image(url: str) -> tuple[str, str]:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    oak_share_url = query_params.get('_oak_share_url', [''])[0]
    goods_id = query_params.get('goods_id', [''])[0]
    return goods_id, oak_share_url


async def is_member_channels(message: types.Message):
    check = list()
    user_chat_id = message.chat.id
    for channel_chat_id in settings.channel_chat_ids:
        sub = await BOT.get_chat_member(chat_id=channel_chat_id, user_id=user_chat_id)
        if sub.status != types.ChatMemberStatus.LEFT:
            check.append(True)
        else:
            check.append(False)
    if all(check):
        return True
    else:
        return False


class APIClient:
    transport: httpx.AsyncHTTPTransport = httpx.AsyncHTTPTransport(retries=3)
    headers: dict = {'accept': 'application/json', 'Content-Type': 'application/json'}
    session: httpx.AsyncClient = httpx.AsyncClient(
        transport=transport,
        timeout=3,
        headers=headers
    )

    def __call__(self) -> httpx.AsyncClient:
        return self.session
