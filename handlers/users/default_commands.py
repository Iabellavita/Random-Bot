from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from app import dp
from keyboards.inline_button import choose


@dp.message_handler(CommandStart())
async def bot_hello(message: types.Message):
    await message.answer("Привіт 👋\nЯ Рандом-бот. Обери потрібну тобі функцію.", parse_mode=types.ParseMode.HTML,
                         reply_markup=choose)


@dp.message_handler()
async def bot_random(message: types.Message):
    await message.answer("Звертайтесь по ділу /start\nабо ідіть геть 😡", parse_mode=types.ParseMode.HTML)
