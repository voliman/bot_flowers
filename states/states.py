from aiogram.dispatcher.filters.state import State, StatesGroup


class FormState(StatesGroup):
    state_registration = State()
    state_start_menu = State()
    state_select_filter = State()
    state_select_category = State()
    state_out = State()
    state_favorite = State()
