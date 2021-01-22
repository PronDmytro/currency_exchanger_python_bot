from telebot import types

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key1 = types.KeyboardButton('Підписатися на повідомлення')
key2 = types.KeyboardButton('Отримати курс')
key3 = types.KeyboardButton('Команди')
key4 = types.KeyboardButton('Конвертація')
main_keyboard.add(key1, key2, key3, key4)

course_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
item1 = types.KeyboardButton('\U0001F4B5USD\U0001F4B5')
item2 = types.KeyboardButton('\U0001F4B6EUR\U0001F4B6')
item3 = types.KeyboardButton('\U000020BDRUB\U000020BD')
item4 = types.KeyboardButton('\U0001F4B7PLN\U0001F4B7')
course_keyboard.add(item1, item2, item3, item4)

exchange_menu = types.InlineKeyboardMarkup(row_width=1)
exc1 = types.InlineKeyboardButton(text='Гривні в долари', callback_data='uah_to_usd')
exc2 = types.InlineKeyboardButton(text='Гривні в євро', callback_data='uah_to_eur')
exc3 = types.InlineKeyboardButton(text='Гривні в рублі', callback_data='uah_to_rub')
exc4 = types.InlineKeyboardButton(text='Гривні в злоти', callback_data='uah_to_pln')
exc5 = types.InlineKeyboardButton(text='Долари в гривні', callback_data='usd_to_uah')
exc6 = types.InlineKeyboardButton(text='Євро в гривні', callback_data='eur_to_uah')
exc7 = types.InlineKeyboardButton(text='Рублі в гривні', callback_data='rub_to_uah')
exc8 = types.InlineKeyboardButton(text='Злоти в гривні', callback_data='pln_to_uah')
exchange_menu.add(exc1, exc2, exc3, exc4, exc5, exc6, exc7, exc8)

