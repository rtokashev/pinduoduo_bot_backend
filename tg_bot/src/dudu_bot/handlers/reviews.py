import httpx

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from dudu_bot.states.states import Reviews
from dudu_bot.texts import main_texts
from dudu_bot.settings import DP, BOT
from dudu_bot.keyboards import (
    review_cancel_ikm
)
from dudu_bot.settings import settings
from dudu_bot.utils import (
    check_goods_url,
    get_goods_id_goods_image,
    APIClient,
    check_text
)
from dudu_bot.filters import IsNotBanned, IsChannelsSubscriber


@DP.message_handler(
    IsNotBanned(),
    IsChannelsSubscriber(),
    regexp=fr'{main_texts.reviews_btn}',
    state=None)
async def reviews(message: types.Message):
    await message.answer(
        text=main_texts.goods_url_review_txt,
        reply=False,
        disable_web_page_preview=True,
        reply_markup=review_cancel_ikm
    )
    await Reviews.Goods.set()


@DP.message_handler(state=Reviews.Goods, content_types=types.ContentType.ANY)
async def reviews_url(message: types.Message, state: FSMContext):
    if message.content_type == types.message.ContentType.TEXT and await check_goods_url(message.text):
        goods_id, goods_image = await get_goods_id_goods_image(url=message.text)
        await state.update_data(goods_id=goods_id)
        await state.update_data(goods_image=goods_image)
        await message.answer(
            text=main_texts.reviews_text,
            reply_markup=review_cancel_ikm
        )
        await Reviews.Text.set()
    else:
        await message.answer(
            text=main_texts.goods_url_warn_txt,
        )
        await Reviews.Goods.set()


@DP.message_handler(state=Reviews.Text, content_types=types.ContentType.TEXT)
async def reviews_text(message: types.Message, state: FSMContext):
    text = message.text
    if not check_text(text=text):
        request = APIClient()
        data = await state.get_data()
        goods_id = data.get('goods_id')
        goods_image = data.get('goods_image')
        post_data = await BOT.send_message(
            chat_id=settings.reviews_chat_id,
            text=main_texts.reviews_form_txt.format(goods_image, goods_id, goods_id, text),
            reply_to_message_id=True,
            parse_mode='HTML'
        )
        post_id = post_data.message_id
        post_url = settings.reviews_post_url.format(post_id)
        body = {
            "post_id": post_id,
            "post_url": post_url,
            "goods_id": goods_id
        }
        try:
            response = await request.session.post(
                url=f'{settings.api_url}reviews',
                json=body
            )
        except httpx.ConnectError:
            response = None
        if response:
            await message.answer(text=main_texts.reviews_pub_post_txt.format(post_url))
        else:
            await message.reply(
                text=main_texts.error_txt,
                reply=False
            )
        await state.finish()
    else:
        await message.answer(text=main_texts.reviews_warn_text)
        await state.finish()


@DP.callback_query_handler(text="review_cancel", state=Reviews)
async def review_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await state.reset_state()
