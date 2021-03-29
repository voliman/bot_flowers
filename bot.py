import telebot, re, requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
from telebot import types

bot = telebot.AsyncTeleBot('')

keyboardCity = telebot.types.ReplyKeyboardMarkup()
keyboardCity.row('Москва','Избранное')
#keyboardCity.row('Избранное')

keyboardCat1 = telebot.types.ReplyKeyboardMarkup()
keyboardCat1.row('до 5к', 'до 10к', 'до 15к', 'VIP')
keyboardCat1.row('Розы', 'Свадебные', 'Оптом')
keyboardCat1.row('Избранное', 'Назад')

keyboardCat2 = telebot.types.ReplyKeyboardMarkup()
keyboardCat2.row('Авторские','Моно\Дуо','Не имеет Значения')
keyboardCat2.row('Избранное','Назад')

keyboardControl = telebot.types.ReplyKeyboardMarkup()
keyboardControl.row('Еще 3','Предыдущие 3')
keyboardControl.row('Избранное','Назад')

keyboardInline = telebot.types.InlineKeyboardMarkup()
buyButton = telebot.types.InlineKeyboardButton(text='Купить', url='https://yandex.ru')
favoritButton = telebot.types.InlineKeyboardButton(text='В Избранное',url='')
instaButton = telebot.types.InlineKeyboardButton(text='Инстаграмм', url='https://instagramm.com')

@bot.message_handler(commands=['start'])
def startMenu(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, "Привет, " + message.chat.first_name, reply_markup=keyboardCity)
        bot.register_next_step_handler(message, startChain)

def startChain(message):
    if message.text == 'Москва':
        #вывод меню с фильтрами поиском по каталогу
        #кнопки до5000 до10000 до15000 VIP Розы Свадебные КупитьОптом Избранное Назад
        bot.send_message(message.chat.id, "Выберите категорю ", reply_markup = keyboradCat1)
        bot.register_next_step_handler(message, filt)

    if message.text == 'Санкт-Петербург':

        bot.send_message(message.chat.id, '404 Not Found, plz call you administrator', reply_markup = keyboardCat1)
        bot.register_next_step_handler(message, startChain)

    if message.text == 'Избранное':

        bot.register_next_step_handler(message, menuFavorit)

def filt(message):
    
    #вывод второго фильтра
    #кнопки авторскиеБукеты Моно\ДуоБукеты НеимеетЗначения Избранное назад
    
    if message.text == 'Избранное':

        bot.register_next_step_handler(message, menuFavorit)

    elif message.text == 'Назад':

        bot.register_next_step_handler(message, startChain)

    else:
        bot.send_message(messsage.chat.id, "", reply_markup=keyboardCat2)
        bot.register_next_step_handler(message, filt2, message.text)

def filt2(message, cat1):
    # Вывод по 3 картинки
    # Под каждой картинкой 3 кнопки(купить, в избранное, перейти в инсту) + описании картинка(цена)
    # клава: еще 3, предыд 3, назад, избранное

    #Запрос в БД по 2 фильтрам, вывод по 3

    bot.send_message(message.chat.id, "", reply_markup = keyboardControl)
    bot.register_next_step_handler(message, out)

    if message.text == 'Избранное':

        bot.register_next_step_handler(message, menuFavorit)

    if message.text == 'Назад':

        bot.register_next_step_handler(message, startChain)

def out(message)
    # Вывод по 3 картинки
    # Под каждой картинкой 3 кнопки(купить, в избранное, перейти в инсту) + описании картинка(цена)
    # клава: еще 3, предыд 3, назад, избранное

    bot.send_message(message.chat.id, "", reply_markup = keyboardControl)
    bot.register_next_step_handler(message, out)

    if message.text == 'Избранное':

        bot.register_next_step_handler(message, menuFavorit)

    if message.text == 'Назад':

        bot.register_next_step_handler(message, startChain)


bot.polling(none_stop=True, interval=0) 