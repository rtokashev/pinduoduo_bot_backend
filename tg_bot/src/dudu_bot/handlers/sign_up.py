import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from dudu_bot.states.states import UserRegister
from dudu_bot.texts import main_texts
from dudu_bot.settings import DP, BOT
from dudu_bot.keyboards import (
    phone_rkm,
    channel_link_ikm,
    main_rkm,
    reg_rkm
)
from aiogram.utils.exceptions import MessageToDeleteNotFound
from dudu_bot.utils import is_member_channels


@DP.message_handler(regexp=fr'{main_texts.reg_btn}', state=None)
async def sign_up(message: types.Message):
    # check if user registered TODO
    await message.answer(
        text=main_texts.share_phone_txt,
        reply=False,
        reply_markup=phone_rkm
    )
    await UserRegister.Telephone.set()


@DP.message_handler(state=UserRegister.Telephone, content_types=types.ContentType.ANY)
async def telephone(message: types.Message, state: FSMContext):
    if message.content_type == types.message.ContentType.CONTACT:
        contact = json.loads(message.contact.as_json())
        chat_id = message.from_user.id
        phone = contact.get('phone_number')
        username = message.from_user.username
        await state.update_data(chat_id=chat_id)
        await state.update_data(phone=phone)
        await state.update_data(username=username)
        mes = await message.reply(
            text=main_texts.channel_sub_txt,
            reply=False,
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.update_data(message_id=mes.message_id)
        await message.reply(
            text=main_texts.channel_list_txt,
            reply=False,
            reply_markup=channel_link_ikm
        )
        await UserRegister.Channel.set()
    else:
        await message.reply(
            text=main_texts.share_phone_warn_txt,
            reply=False,
            reply_markup=phone_rkm
        )
        await UserRegister.Telephone.set()


@DP.callback_query_handler(text_contains="member", state=UserRegister.Channel)
async def subscribe(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    try:
        message_id = data.get('message_id')
        message_from_id = call.message.chat.id
        await BOT.delete_message(chat_id=message_from_id, message_id=message_id)
    except MessageToDeleteNotFound:
        pass
    await call.message.edit_reply_markup()
    await call.message.delete()
    is_member = await is_member_channels(message=call.message)
    if is_member:
        await call.message.reply(
            text=main_texts.reg_success_txt,
            reply=False,
            reply_markup=main_rkm
        )
        chat_id = data.get('chat_id')
        phone = data.get('phone')
        username = data.get('username')
        # request to rest api TODO
        await state.finish()
    else:
        await call.message.reply(
            text=main_texts.channel_sub_txt,
            reply=False,
            reply_markup=channel_link_ikm
        )
        await UserRegister.Channel.set()


@DP.callback_query_handler(text="reg_cancel", state=UserRegister)
async def cancel_btn(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await state.reset_state()
    await call.message.answer(
        text=main_texts.cancel_btn,
        reply=False,
        reply_markup=reg_rkm
    )
