from collections import namedtuple


MainTexts = namedtuple(
    'MainTexts',
    'share_phone_btn share_phone_txt welcome_txt reg_txt reg_btn purchase_reg_btn referral_btn subscribe_btn ask_btn '
    'about_bot_btn channel_sub_txt shopping_channel_btn news_channel_btn cancel_btn imember_btn channel_list_txt '
    'reg_success_txt share_phone_warn_txt'
)

main_texts = MainTexts(
    share_phone_btn='📱 Поделиться контактом',
    share_phone_txt='<b>✅ Поделитесь своим номером телефона</b>\n<i>*Нажмите кнопку снизу</i> 👇',
    share_phone_warn_txt='<b>⚠️ Поделитесь своим номером телефона</b>\n<i>*Нажмите кнопку снизу</i> 👇',
    welcome_txt='Добро пожаловать!\n\nЯ чат-бот <b>DuDuBot</b>, личный помощник для совместных покупок в Pinduoduo 🛍'
                '\n\n <a href="https://www.youtube.com/watch?v=RG6cWQ2O5QY">Промо</a>',
    reg_txt='<b>✅ Нажмите кнопку регистрации, чтобы начать пользоваться ботом</b> 👇',
    reg_btn='➕ Регистрация',
    purchase_reg_btn='🛍 Совместная покупка',
    referral_btn='👨‍👦‍👦 Реферальная система',
    subscribe_btn='💳 Купить подписку',
    ask_btn='📣 Вопросы и предложения',
    about_bot_btn='↗ Подробнее о боте',
    channel_sub_txt='<b>✅ Обязательным условием использования бота является подписка на следующие каналы бота:</b>',
    channel_list_txt='<i>*Пройдите по ссылкам на каналы, подпишитесь и нажмите я подписался</i>👇',
    shopping_channel_btn='↗ DuDuBot - Shopping',
    news_channel_btn='↗ DuDuBot - Channel',
    cancel_btn='❌ Отмена',
    imember_btn='☑️ Я подписался',
    reg_success_txt='<b>Спасибо за регистрацию</b> 👍'
)