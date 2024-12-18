from collections import namedtuple


MainTexts = namedtuple(
    'MainTexts',
    'share_phone_btn share_phone_txt welcome_txt reg_txt reg_btn purchase_reg_btn referral_btn subscribe_btn ask_btn '
    'about_bot_btn channel_sub_txt shopping_channel_btn news_channel_btn cancel_btn imember_btn channel_list_txt '
    'reg_success_txt share_phone_warn_txt goods_url_txt request_form_txt post_confirm_btn post_cancel_btn '
    'goods_url_warn_txt shopping_pub_post_txt error_txt is_banned_txt warn_limit_txt reviews_btn goods_url_review_txt '
    'dudu_cargo_btn reviews_text reviews_form_txt reviews_pub_post_txt reviews_warn_text cargo_info_txt '
    'cargo_address_txt cargo_address_btn client_notify_btn client_notify_txt calc_data_txt reviews_already_add_txt '
    'purchase_already_add_txt'
)

main_texts = MainTexts(
    share_phone_btn='📱 Поделиться контактом',
    share_phone_txt='<b>✅ Поделитесь своим номером телефона</b>\n<i>*Нажмите кнопку снизу</i> 👇',
    share_phone_warn_txt='<b>⚠️ Поделитесь своим номером телефона</b>\n<i>*Нажмите кнопку снизу</i> 👇',
    welcome_txt='Добро пожаловать!\n\nЯ чат-бот <b>DuDuBot</b>, личный помощник для покупок в Pinduoduo 🛍',
    reg_txt='<b>✅ Нажмите кнопку регистрации, чтобы начать пользоваться ботом</b> 👇',
    reg_btn='➕ Регистрация',
    purchase_reg_btn='🛍 Совместная покупка',
    referral_btn='👨‍👦‍👦 Реферальная система',
    subscribe_btn='💳 Купить подписку',
    ask_btn='📣 Вопросы и предложения',
    reviews_btn='⭐️️ Отзывы товаров',
    dudu_cargo_btn='🚛 DuDu Cargo',
    about_bot_btn='↗ Подробнее о боте',
    channel_sub_txt='<b>✅ Обязательным условием использования бота является подписка на следующие каналы бота:</b>',
    channel_list_txt='<i>*Пройдите по ссылкам на каналы, подпишитесь и нажмите я подписал(ась)ся</i>👇',
    shopping_channel_btn='↗ DuDuBot - Shopping',
    news_channel_btn='↗ DuDuBot - Channel',
    cancel_btn='❌ Отмена',
    imember_btn='☑️ Я подписал(ась)ся',
    reg_success_txt='<b>Спасибо за регистрацию</b> 👍',
    goods_url_txt='<b>✅ Передайте ссылку товара из Pinduoduo</b>',
                  # '\n<i>*Посмотрите <a href="https://www.youtube.com/watch?v=RG6cWQ2O5QY">видео инструкцию</a> '
                  # 'как сделать заявку на совместную покупку</i>',
    request_form_txt='<b>🆔:</b> <a href="{}">#{}</a>'
                     '\n\n<b>📦 Товар:</b> <a href="https://mobile.yangkeduo.com/goods1.html?goods_id={}">'
                     '<b>Ссылка на товар</b></a>\n\n<i>*Обсуждайте детали совместной покупки внизу в комментарии</i>👇',
    post_confirm_btn='🟩 Подтвердить',
    post_cancel_btn='🟥 Отменить',
    goods_url_warn_txt='<b>⚠️ Неверная ссылка на товар</b>',
    shopping_pub_post_txt='<b>Спасибо 👍 Ваша публикация опубликовано, перейдите к публикации по ссылке: {}</b>\n\n'
                 '<i>*Данная публикация автоматический удалится из канала через 5 дней</i>',
    error_txt='<b>⚠️ Техническая неполадка попробуйте позже</b>',
    is_banned_txt='<b>⚠️ Вы заблокированы!</b>',
    warn_limit_txt='<b>⚠️ Вы исчерпали свой лимит (3 запроса в день), попробуйте завтра</b>',
    goods_url_review_txt='<b>✅ Передайте ссылку товара из Pinduoduo</b>',
                  # '\n<i>*Посмотрите <a href="https://www.youtube.com/watch?v=RG6cWQ2O5QY">видео инструкцию</a> '
                  # 'как добавить отзыв на купленный товар</i>',
    reviews_text='<b>✅ Поделитесь Вашим мнением о данном товаре</b>\n<i>*Не более 250 слов</i>',
    reviews_form_txt='<b>🆔:</b> <a href="{}">#{}</a>'
                     '\n\n<b>📦 Товар:</b> <a href="https://mobile.yangkeduo.com/goods1.html?goods_id={}">'
                     '<b>Ссылка на товар</b></a>'
                     '\n\n<b>⭐️ Отзыв:</b> {}'
                     '\n\n<i>*Если Вы также приобретали данный товар, напишите Ваш отзыв внизу в комментарии</i>👇',
    reviews_pub_post_txt='<b>Спасибо 👍 Ваш отзыв опубликован, перейдите к публикации по ссылке: {}</b>\n\n'
                 '<i>*Спасибо Вы помогли другим людям не ошибится в выборе товара</i>',
    reviews_warn_text='<b>⚠️ Ваш текст отзыва содержит недопустимые ссылки или символы</b>',
    cargo_info_txt=r"""
    Добро пожаловать! в 🚛 DuDu Cargo

    💴 <b>Тариф и цены:</b>
    
    📍 Астана - 5$ \ 1кг.
    
    <i>* цена с учетом доставки в город, дополнительно ничего платить не нужно
    * вес расчитывается за совокупность Ваших товаров не по отдельности (если будет несколько заказов), если будет меньше 1кг то округляется как кг.
    * ограничении по весу нет
    * в тариф не входит цена за дополнительную упаковку хрупких вещей (об этом надо заранее предупредить)</i>
    
    
    ❌ <b>Запрещенные товары для заказа:</b>
    
    - Продукты питания (кроме сухих продуктов)
    - Овощи-фрукты
    - Лекарственные препараты, наркотики
    - Холодное оружие, все виды ножей (взрывчатые вещества)
    - Химические жидкости
    - Брендовые вещи (в большом количестве)
    - Сигареты (vape, электронные)
    - Стекла
    
    
    🕒 <b>Сроки доставки:</b>
    
    10 - 15 дней (после того как ваш заказ прибудет на склад в Китае)
    """,
    cargo_address_txt='<b><i>*Посмотрите <a href="https://www.youtube.com/watch?v=RG6cWQ2O5QY">видео инструкцию</a> '
                  'как добавить код и адрес в Pinduoduo</i></b>'
                  '\n\n<b>1. 0909-DUDU-AST</b>'
                  '\n\n<b>2. 15894110023</b>'
                  '\n\n<b>3. 广东省  佛山市  南海区</b>'
                  '\n\n<b>4. 大沥镇建设大道敦豪物流D2栋33一35仓 (Astana {chat_id} {phone})</b>',
    cargo_address_btn='🟩 Получить личный код(адрес) Pinduoduo',
    client_notify_btn='📣 Оповестить',
    client_notify_txt='Приветствую 👋. Ваши товары прибыли в город. Спасибо за выбор 🚛 DuDu Cargo'
                      '\n\n\n\n<b>⚖️ Общий вес товара:  {weight} кг.</b>'
                      '\n\n<b>💰 К оплате:  {price} ₸</b>'
                      '\n\n<b>🧑‍🚀 Служба поддержки:  @dudubot_support</b>'
                      '\n\n<b>📍 Откуда забрать:  {address}</b>',
    calc_data_txt='<b>✅ Введите (chat_id, вес товаров, цену к оплате) через запятой:</b>',
    reviews_already_add_txt='<b>Для данного товара уже имеется отзыв. Пройдите по ссылке: {}</b>'
                            '\n<i>Оставьте свой отзыв внизу комментарии поста</i>',
    purchase_already_add_txt='<b>Для данного товара уже создана заявка на совместную покупку. '
                             'Пройдите по ссылке: {}</b>'
                            '\n<i>Обсудите детали внизу комментарии поста</i>',
)
