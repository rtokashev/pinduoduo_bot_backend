from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from dudu_bot.texts import main_texts


reg_rkm = ReplyKeyboardMarkup(
    [
        [KeyboardButton(main_texts.reg_btn)]
    ], resize_keyboard=True
)

main_rkm = ReplyKeyboardMarkup(
    [
        [KeyboardButton(main_texts.purchase_reg_btn)],
        [KeyboardButton(main_texts.referral_btn)],
        [KeyboardButton(main_texts.subscribe_btn)],
        [KeyboardButton(main_texts.ask_btn)],
    ], resize_keyboard=True,
)

cancel_ikb = InlineKeyboardButton(text=main_texts.cancel_btn, callback_data="reg_cancel")
i_member_ikb = InlineKeyboardButton(text=main_texts.imember_btn, callback_data="member")
about_bot_ikb = InlineKeyboardButton(text=main_texts.about_bot_btn, url='https://t.me/arzanal_channel')
shopping_channel_ikb = InlineKeyboardButton(text=main_texts.shopping_channel_btn, url='https://t.me/+2v2hiKpZCTpjMzYy')
news_channel_ikb = InlineKeyboardButton(text=main_texts.news_channel_btn, url='https://t.me/+tL4k7RI9kBtmZmUy')

about_bot_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [about_bot_ikb]
    ]
)

phone_rkm = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=main_texts.share_phone_btn, request_contact=True)]
    ], resize_keyboard=True
)

channel_link_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [shopping_channel_ikb, news_channel_ikb],
        [i_member_ikb],
        [cancel_ikb]
    ]
)