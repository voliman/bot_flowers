import pymysql
import configparser
import aiogram
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from keyboard import markups
from states import states

config = configparser.ConfigParser()
config.read("config.ini")

DB_HOST = config["Datebase"]["host"]
DB_USERNAME = config["Datebase"]["username"]
DB_PASSWORD = config["Datebase"]["password"]
DB_NAME = config["Datebase"]["name_db"]

connection = pymysql.connect(
    host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD,
    db=DB_NAME, autocommit=True
)
cursor = connection.cursor(pymysql.cursors.DictCursor)

API_TOKEN = "1607900006:AAFUzmWn5lruUEsVkRWYa_fvZw52cFA9xzE"

storage = RedisStorage2()
bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot, storage=storage)
dp.middleware.setup(aiogram.middlewares.BaseMiddleware())

FormState = states.FormState()


@dp.message_handler(commands=['start'], state='*')
async def process_start_command(message: aiogram.types.Message):
    sql = "SELECT COUNT(*) FROM users WHERE `user.id` = " + \
        str(message.from_user.id) + ";"

    cursor.execute(sql)
    result = cursor.fetchone()

    msg_text = '''Привет! 👋
🤖 Я бот-магазин по подаже товаров любой категории.

🛍️ Чтобы перейти в каталог и выбрать приглянувшиеся товары возпользуйтесь командой /menu.'''

    if result['COUNT(*)'] == 0:
        await message.answer(msg_text,
                             reply_markup=aiogram.types.ReplyKeyboardRemove())

        sql = "1INSERT INTO `users` (`id`, `user.id`, `chat_id`, `name`) VALUES (NULL, " + str(
            message.from_user.id) + ", '" + str(message.chat.id) + "', '" + message.chat.first_name + "');"
        cursor.execute(sql)

    else:
        await message.answer(msg_text,
                             reply_markup=aiogram.types.ReplyKeyboardRemove())


@dp.message_handler(commands=['help'], state='*')
async def process_help_command(message: aiogram.types.Message):
    await message.answer("Напиши мне что-нибудь")


@dp.message_handler(commands=['menu'], state='*')
async def process_start_menu(message: aiogram.types.Message):
    await message.answer('Выберите город', reply_markup=markups.city_markup())
    await FormState.state_start_menu.set()
    await FormState.next()


@dp.message_handler(state=FormState.state_select_filter)
async def process_select_filter(message: aiogram.types.Message):
    await message.answer('Выберите категорию',
                         reply_markup=markups.filter_markup())
    await FormState.next()


@dp.message_handler(state=FormState.state_select_category)
async def process_select_category(message: aiogram.types.Message):
    if message.text == markups.filter_category[6]:
        await message.answer('Если вы хотите приобрести цветы оптом, пожалуйста, напишите нам @flowboo_support')
    elif message.text == markups.filter_category[4]:
        await message.answer('Rose out', reply_markup=markups.control_markup())
        await FormState.state_out.set()
    elif message.text == markups.filter_category[5]:
        await message.answer('Marry out', reply_markup=markups.control_markup())
        await FormState.state_out.set()
    else:
        await message.answer('Выберите 2 категрию',
                             reply_markup=markups.category_markup())
        await FormState.next()


@dp.message_handler(state=FormState.state_out)
async def process_out(message: aiogram.types.Message):
    if message.text == markups.back_message:
        await message.answer('Выберите категорию',
                             reply_markup=markups.filter_markup())
        await FormState.state_select_filter.set()
        await FormState.next()
    else:
        await message.answer('Out', reply_markup=markups.control_markup())

if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
