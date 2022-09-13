from aiogram import executor

from config import dp
from utils.default_commands import set_default_commands
from handlers.users import default_commands
from handlers.users import work_with_clients


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
