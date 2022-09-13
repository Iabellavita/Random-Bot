from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery
from app import dp
from keyboards.inline_button import choose, cancel
from states import Words
from states import Digits
import random


def random_choice(data: str):
    if ';' in data:
        choices = data.split(';')
        choice = random.choice(choices)
    elif '-' in data:
        choices = data.split('-')
        choice = random.randint(int(choices[0]), int(choices[1]))
    return choice


@dp.callback_query_handler(text="words")
async def cancel_button(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        "☝️ Відправ виборку слів або словосполучень через крапку з комою, як на прикладі нижче\n\n"
        "<code>Словосполучення 1;Словосполучення 2;Словосполучення 3</code>",
        parse_mode=types.ParseMode.HTML, reply_markup=cancel)
    await Words.Q1.set()


@dp.callback_query_handler(text="digits")
async def cancel_button(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        "☝️ Відправ свій чисельний діапазон, як на прикладі нижче\n\n"
        "<code>6543-99999</code>",
        parse_mode=types.ParseMode.HTML, reply_markup=cancel)
    await Digits.Q1.set()


@dp.callback_query_handler(text="cancel", state='*')
async def cancel_button(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Обери потрібну тобі функцію 👇", reply_markup=choose,
                              parse_mode=types.ParseMode.HTML)


@dp.message_handler(state=Words.Q1)
async def check_title(message: types.Message, state: FSMContext):
    try:
        choice = random_choice(message.text)
        await message.answer("🎣 Мій вибір:\n\n"
                             f"{choice}", parse_mode=types.ParseMode.HTML)
    except:
        await message.answer("🌶 Дотримуйся правил вводу. Перевір вхідні дані.", parse_mode=types.ParseMode.HTML)

    await state.finish()
    await message.answer("Обери потрібну тобі функцію 👇", reply_markup=choose,
                         parse_mode=types.ParseMode.HTML)


@dp.message_handler(state=Digits.Q1)
async def cancel_button(message: types.Message, state: FSMContext):
    try:
        choice = random_choice(message.text)
        await message.answer("🧩 Мій вибір:\n\n"
                             f"{choice}", parse_mode=types.ParseMode.HTML)
    except:
        await message.answer("🌶 Дотримуйся правил вводу. Перевір вхідні дані.", parse_mode=types.ParseMode.HTML)

    await state.finish()
    await message.answer("Обери потрібну тобі функцію 👇", reply_markup=choose,
                         parse_mode=types.ParseMode.HTML)
