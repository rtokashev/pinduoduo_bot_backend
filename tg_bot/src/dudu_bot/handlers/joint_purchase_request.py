import httpx

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from dudu_bot.states.states import JointPurchaseRequest
from dudu_bot.texts import main_texts
from dudu_bot.settings import DP, BOT
from dudu_bot.keyboards import (
    req_cancel_ikm,
    post_request_ikm
)
from dudu_bot.settings import settings
from dudu_bot.utils import (
    check_goods_url,
    get_goods_id_goods_image,
    APIClient
)
from dudu_bot.filters import IsNotBanned, IsChannelsSubscriber
from dudu_bot.utils import APIClient


@DP.message_handler(
    IsNotBanned(),
    IsChannelsSubscriber(),
    regexp=fr'{main_texts.purchase_reg_btn}',
    state=None)
async def purchase(message: types.Message):
    request = APIClient()
    chat_id = message.chat.id
    try:
        response = await request.session.get(
            url=f'{settings.api_url}users/{chat_id}/limits',
        )
    except httpx.ConnectError:
        response = None
    if response:
        if response.json().get('daily_requests_count', 0) > 0:
            await message.answer(
                text=main_texts.goods_url_txt,
                reply=False,
                disable_web_page_preview=True,
                reply_markup=req_cancel_ikm
            )
            await JointPurchaseRequest.Request.set()
        else:
            await message.answer(
                text=main_texts.warn_limit_txt,
            )
    else:
        await message.reply(
            text=main_texts.error_txt,
            reply=False
        )


@DP.message_handler(state=JointPurchaseRequest.Request, content_types=types.ContentType.ANY)
async def request_purchase(message: types.Message, state: FSMContext):
    if message.content_type == types.message.ContentType.TEXT and await check_goods_url(message.text):
        goods_id, goods_image = await get_goods_id_goods_image(url=message.text)
        await state.update_data(goods_id=goods_id)
        await state.update_data(goods_image=goods_image)
        await message.answer(
            text=main_texts.request_form_txt.format(goods_image, goods_id, goods_id),
            reply_markup=post_request_ikm,
        )
        await JointPurchaseRequest.Post.set()
    else:
        await message.answer(
            text=main_texts.goods_url_warn_txt
        )
        await JointPurchaseRequest.Request.set()


@DP.callback_query_handler(text_contains="post_confirm", state=JointPurchaseRequest.Post)
async def post(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    request = APIClient()
    data = await state.get_data()
    goods_id = data.get('goods_id')
    goods_image = data.get('goods_image')
    post_data = await BOT.send_message(
        chat_id=settings.channel_chat_ids[0],
        text=main_texts.request_form_txt.format(goods_image, goods_id, goods_id),
        reply_to_message_id=True,
        parse_mode='HTML'
    )
    goods_url = settings.goods_url.format(goods_id)
    post_id = post_data.message_id
    chat_id = call.message.chat.id
    post_url = settings.shopping_post_url.format(post_id)
    body = {
        'chat_id': chat_id,
        "link": goods_url,
        "goods_id": goods_id,
        "photo": goods_image,
        "post_id": post_id,
        "post_url": post_url
    }
    try:
        response = await request.session.post(
            url=f'{settings.api_url}purchases',
            json=body
        )
    except httpx.ConnectError:
        response = None
    if response:
        await call.message.answer(text=main_texts.shopping_pub_post_txt.format(post_url))
    else:
        await call.message.reply(
            text=main_texts.error_txt,
            reply=False
        )
    await state.finish()


@DP.callback_query_handler(text="post_cancel", state=JointPurchaseRequest)
async def post_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await state.reset_state()
    await call.message.answer(text=main_texts.post_cancel_btn)


@DP.callback_query_handler(text="req_cancel", state=JointPurchaseRequest)
async def req_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await state.reset_state()
