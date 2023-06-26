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
    get_goods_id_goods_image
)


@DP.message_handler(regexp=fr'{main_texts.purchase_reg_btn}', state=None)
async def purchase(message: types.Message):
    # check if user registered TODO
    await message.answer(
        text=main_texts.goods_url_txt,
        reply=False,
        disable_web_page_preview=True,
        reply_markup=req_cancel_ikm
    )
    await JointPurchaseRequest.Request.set()


@DP.message_handler(state=JointPurchaseRequest.Request, content_types=types.ContentType.ANY)
async def request(message: types.Message, state: FSMContext):
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
    post_url = settings.post_url.format(post_id)
    await call.message.answer(text=main_texts.pub_post_txt.format(post_url))
    await state.finish()


@DP.callback_query_handler(text="post_cancel", state=JointPurchaseRequest)
async def post_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await state.reset_state()
    await call.message.answer(text=main_texts.post_cancel_btn)


@DP.callback_query_handler(text="req_cancel", state=JointPurchaseRequest)
async def post_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await state.reset_state()
