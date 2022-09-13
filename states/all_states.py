from aiogram.dispatcher.filters.state import StatesGroup, State


class Words(StatesGroup):
    Q1 = State()
    Q2 = State()


class Digits(StatesGroup):
    Q1 = State()
    Q2 = State()
