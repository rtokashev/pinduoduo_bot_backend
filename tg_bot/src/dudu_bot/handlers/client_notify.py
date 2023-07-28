import httpx

from aiogram import types
from dudu_bot.texts import main_texts
from dudu_bot.settings import DP, settings
from dudu_bot.keyboards import notify_cancel_ikm
from dudu_bot.utils import APIClient
from dudu_bot.states.states import ClientNotify
from aiogram.dispatcher import FSMContext


@DP.message_handler(
    regexp=fr'{main_texts.client_notify_btn}',
    state=None
)
async def notifier(message: types.Message):
    await message.answer(
        text=main_texts.calc_data_txt,
        reply_markup=notify_cancel_ikm,
    )
    await ClientNotify.Calculation.set()


@DP.message_handler(state=ClientNotify.Calculation, content_types=types.ContentType.TEXT)
async def notify_calculation(message: types.Message, state: FSMContext):
    admin_chat_id = message.chat.id
    data = message.text.split(',')
    chat_id = int(data[0].strip())
    weight = float(data[1].strip())
    price = int(data[2].strip())
    await state.update_data(chat_id=chat_id)
    await state.update_data(weight=weight)
    await state.update_data(price=price)
    await message.answer(
                text=main_texts.client_notify_txt.format(
                    weight=weight,
                    price=price,
                    address=settings.admin_addresses.get(admin_chat_id)
                ),
            )


@DP.callback_query_handler(text="notify_cancel", state=ClientNotify)
async def notify_cancel_btn(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await state.reset_state()
