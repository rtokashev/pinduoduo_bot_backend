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
        [KeyboardButton(main_texts.reviews_btn)],
        [KeyboardButton(main_texts.dudu_cargo_btn)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

reg_cancel_ikb = InlineKeyboardButton(text=main_texts.cancel_btn, callback_data="reg_cancel")
req_cancel_ikb = InlineKeyboardButton(text=main_texts.cancel_btn, callback_data="req_cancel")
notify_cancel_ikb = InlineKeyboardButton(text=main_texts.cancel_btn, callback_data="notify_cancel")
review_cancel_ikb = InlineKeyboardButton(text=main_texts.cancel_btn, callback_data="review_cancel")
i_member_ikb = InlineKeyboardButton(text=main_texts.imember_btn, callback_data="member")
post_confirm_ikb = InlineKeyboardButton(text=main_texts.post_confirm_btn, callback_data="post_confirm")
post_cancel_ikb = InlineKeyboardButton(text=main_texts.post_cancel_btn, callback_data="post_cancel")
about_bot_ikb = InlineKeyboardButton(text=main_texts.about_bot_btn, url='https://t.me/arzanal_channel')
shopping_channel_ikb = InlineKeyboardButton(text=main_texts.shopping_channel_btn, url='https://t.me/+2v2hiKpZCTpjMzYy')
news_channel_ikb = InlineKeyboardButton(text=main_texts.news_channel_btn, url='https://t.me/+tL4k7RI9kBtmZmUy')
cargo_code_ikb = InlineKeyboardButton(text=main_texts.cargo_address_btn, callback_data="cargo_code")

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
        [reg_cancel_ikb]
    ]
)

filter_channel_link_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [shopping_channel_ikb, news_channel_ikb],
    ]
)

req_cancel_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [req_cancel_ikb]
    ]
)

notify_cancel_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [notify_cancel_ikb]
    ]
)

review_cancel_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [review_cancel_ikb]
    ]
)

post_request_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [post_confirm_ikb, post_cancel_ikb]
    ]
)

cargo_code_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [cargo_code_ikb]
    ]
)

admin_rkm = ReplyKeyboardMarkup(
    [
        [KeyboardButton(main_texts.client_notify_btn)],
        [KeyboardButton(main_texts.purchase_reg_btn)],
        [KeyboardButton(main_texts.reviews_btn)],
        [KeyboardButton(main_texts.dudu_cargo_btn)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)