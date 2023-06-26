from collections import namedtuple


MainTexts = namedtuple(
    'MainTexts',
    'share_phone_btn share_phone_txt welcome_txt reg_txt reg_btn purchase_reg_btn referral_btn subscribe_btn ask_btn '
    'about_bot_btn channel_sub_txt shopping_channel_btn news_channel_btn cancel_btn imember_btn channel_list_txt '
    'reg_success_txt share_phone_warn_txt goods_url_txt request_form_txt post_confirm_btn post_cancel_btn '
    'goods_url_warn_txt pub_post_txt'
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
    channel_list_txt='<i>*Пройдите по ссылкам на каналы, подпишитесь и нажмите я подписал(ась)ся</i>👇',
    shopping_channel_btn='↗ DuDuBot - Shopping',
    news_channel_btn='↗ DuDuBot - Channel',
    cancel_btn='❌ Отмена',
    imember_btn='☑️ Я подписал(ась)ся',
    reg_success_txt='<b>Спасибо за регистрацию</b> 👍',
    goods_url_txt='<b>✅ Передайте ссылку товара из Pinduoduo</b>'
                  '\n<i>*Посмотрите <a href="https://www.youtube.com/watch?v=RG6cWQ2O5QY">видео инструкцию</a> '
                  'как сделать заявку на совместную покупку</i>',
    request_form_txt='<b>🆔:</b> <a href="{}">#{}</a>'
                     '\n\n<b>📦 Товар:</b> <a href="https://mobile.yangkeduo.com/goods1.html?goods_id={}">'
                     '<b>Ссылка на товар</b></a>\n\n<i>*Обсуждайте детали совместной покупки внизу в комментарии</i>👇',
    post_confirm_btn='🟩 Подтвердить',
    post_cancel_btn='🟥 Отменить',
    goods_url_warn_txt='<b>⚠️ Неверная ссылка на товар</b>',
    pub_post_txt='<b>Спасибо 👍 Ваша публикация опубликовано, перейдите к публикации по ссылке: {}</b>\n\n'
                 '<i>*Данная публикация автоматический удалится из канала через 5 дней</i>'
)