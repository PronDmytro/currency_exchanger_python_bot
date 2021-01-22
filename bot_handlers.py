import telebot
from config import TOKEN
import keyboard
import data

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    msg = bot.send_message(
        chat_id=message.chat.id,
        text='Доброго дня, ' + message.chat.first_name,
        reply_markup=keyboard.main_keyboard
    )


@bot.message_handler(commands=['help'])
def help(message):
    msg = bot.send_message(
        chat_id=message.chat.id,
        text='\U0000260EДля зв\'язку писати: @LoLKeKCkEkk'
    )


@bot.message_handler(commands=['pay'])
def pay(message):
    msg = bot.send_message(
        chat_id=message.chat.id,
        text='Для підтримки:\n5168 0010 1005 3507\nВельми вам дякую😚'
    )


@bot.message_handler(commands=['notifications_on'])
def notifications_on(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Наразі ця функція не доступна.\n'
             'Щоб присвидшити вихід нових функції ви можете зробити добровільний внесок.\n'
             'Деталі: /pay'
    )


@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Бот має такі комади:'
             '\n/start'
             '\n/help'
             '\n/notifications_on'
    )


@bot.message_handler(content_types=['text'])
def step1(message):
    text = message.text.lower()

    if text == 'отримати курс':
        msg = bot.send_message(message.chat.id,
                               "Дізнатися актуальний курс валют від Monobank",
                               reply_markup=keyboard.course_keyboard
                               )
        bot.register_next_step_handler(msg, process_coin_step)
    elif text == 'команди':
        commands(message)
    elif text == 'підписатися на повідомлення':
        notifications_on(message)
    elif text == 'конвертація':
        bot.send_message(
            chat_id=message.chat.id,
            text='Виберіть порібну операцію',
            reply_markup=keyboard.exchange_menu,
        )
    else:
        msg = bot.send_message(
            chat_id=message.chat.id,
            text='Не можу распозпізнати команду!',
            reply_markup=keyboard.main_keyboard
        )


def process_coin_step(message):
    message.text = message.text[1:4]
    text = message.text.lower()
    bot.send_message(chat_id=message.chat.id,
                     text=data.course(text),
                     reply_markup=keyboard.main_keyboard
                     )


############
# grn to usd#
@bot.callback_query_handler(func=lambda call: call.data == 'uah_to_usd')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в гривнях, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_usd_from_uah)


def get_usd_from_uah(msg):
    try:
        uah = float(msg.text)
        bot.send_message(msg.chat.id,
                         text=f'На {uah} гривень ви можете купити {data.usd.exchange_from(uah)}$',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_usd_from_uah)


############
# grn to eur#
@bot.callback_query_handler(func=lambda call: call.data == 'uah_to_eur')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в гривнях, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_eur_from_uah)


def get_eur_from_uah(msg):
    try:
        uah = float(msg.text)
        bot.send_message(msg.chat.id, text=f'На {uah} гривень ви можете купити {data.eur.exchange_from(uah)}€',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_eur_from_uah)


############
# grn to rub#
@bot.callback_query_handler(func=lambda call: call.data == 'uah_to_rub')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в гривнях, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_rub_from_uah)


def get_rub_from_uah(msg):
    try:
        uah = float(msg.text)
        bot.send_message(msg.chat.id, text=f'На {uah} гривень ви можете купити {data.rub.exchange_from(uah)}₽',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_rub_from_uah)


############
# grn to pln#
@bot.callback_query_handler(func=lambda call: call.data == 'uah_to_pln')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в гривнях, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_pln_from_uah)


def get_pln_from_uah(msg):
    try:
        uah = float(msg.text)
        bot.send_message(msg.chat.id, text=f'На {uah} гривень ви можете купити {data.pln.exchange_from(uah)}zł',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_pln_from_uah)


############
# usd to grn#
@bot.callback_query_handler(func=lambda call: call.data == 'usd_to_uah')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в доларах, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_uah_from_usd)


def get_uah_from_usd(msg):
    try:
        usd = float(msg.text)
        bot.send_message(msg.chat.id,
                         text=f'На {usd} доларів ви можете купити {data.usd.exchange_to(usd)}₴',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_uah_from_usd)


############
# eur to grn#
@bot.callback_query_handler(func=lambda call: call.data == 'eur_to_uah')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в євро, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_uah_from_eur)


def get_uah_from_eur(msg):
    try:
        eur = float(msg.text)
        bot.send_message(msg.chat.id, text=f'На {eur} євро ви можете купити {data.eur.exchange_to(eur)}₴',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_uah_from_eur)


############
# rub to grn#
@bot.callback_query_handler(func=lambda call: call.data == 'rub_to_uah')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в рублях, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_uah_from_rub)


def get_uah_from_rub(msg):
    try:
        rub = float(msg.text)
        bot.send_message(msg.chat.id, text=f'На {rub} рублів ви можете купити {data.rub.exchange_to(rub)}₴',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_uah_from_rub)


############
# pln to grn#
@bot.callback_query_handler(func=lambda call: call.data == 'pln_to_uah')
def step2(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                text='Введіть суму в злотих, яку хочете обміняти',
                                message_id=call.message.id,
                                )
    bot.register_next_step_handler(message=msg, callback=get_uah_from_pln)


def get_uah_from_pln(msg):
    try:
        pln = float(msg.text)
        bot.send_message(msg.chat.id, text=f'На {pln} злотих ви можете купити {data.pln.exchange_to(pln)}₴',
                         reply_markup=keyboard.main_keyboard,
                         parse_mode="Markdown"
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text='Треба ввести число. Спробуйте ще раз',
                               )
        bot.register_next_step_handler(message=msg, callback=get_uah_from_pln)


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()
