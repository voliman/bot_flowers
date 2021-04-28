import aiogram
from bot import dp
from states import states
from keyboard import markups

FormState = states.FormState()


@dp.message_handler(commands=['menu'], state='*')
async def process_start_menu(message: aiogram.types.Message):
    await message.answer('Выберите город', reply_markup=markups.city_markup())
    await FormState.state_start_menu.set()
    await FormState.next()


@dp.message_handler(state=FormState.state_select_filter)
async def process_select_filter(message: aiogram.types.Message):
    await message.answer('Выберите категорию', reply_markup=markups.filter_markup())
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


@dp.message_handler(state=FormState.state_out)
async def process_out(message: aiogram.types.Message):
    if message.text == markups.back_message:
        await message.answer('Выберите категорию', reply_markup=markups.filter_markup())
        await FormState.state_select_filter.set()
        await FormState.next()
    else:
        await message.answer('Out', reply_markup=markups.control_markup())
