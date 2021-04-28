from aiogram.types import ReplyKeyboardMarkup

favorite_message = '⭐️Избранное'
back_message = '🔙Назад'
prev_message = '👈Предыдущие 3'
next_message = '👉Еще 3'

city = ['🌆Москва', '']

filter_category = ['🌿До 5000 рублей', '☘️До 10000 рублей',
                   '🍀До 15000 рублей', '🌴VIP', '🌹Розы', '🌸Свадебные', '🌳Оптом']

category = ['💐Авторские букеты', '🌺Монобукеты',
            '🌾Цветочные композиции', '🤷Не имеет значения']


def control_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(prev_message, next_message)
    markup.row(back_message, favorite_message)

    return markup


def city_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in city:
        markup.row(item)

    markup.row(favorite_message)

    return markup


def filter_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(filter_category[0], filter_category[1], filter_category[2])
    markup.row(filter_category[3], filter_category[4])
    markup.row(filter_category[5], filter_category[6])
    markup.row(back_message, favorite_message)

    return markup


def category_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    for item in category:
        markup.row(item)

    markup.row(back_message, favorite_message)

    return markup
