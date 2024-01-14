from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv
import os
from state.register import RegisterState
from utils.commands import set_commands
from handlers.start import get_start
from handlers.register import start_register, register_name, register_сabinetNumber
from aiogram.filters import Command

from state.register import RegisterState

load_dotenv()


token = os.getenv("TOKEN")
print("token", token)

admin_id = os.getenv("ADMIN_ID")


bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text="Бот запущен")


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands="start"))

# Регистрируем хендлеры регистрации
dp.message.register(start_register, F.text == "Зарегистрироваться")
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_сabinetNumber, RegisterState.сabinetNumber)


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
