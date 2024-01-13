from aiogram import Bot, Dispatcher, types

import asyncio

TOKEN = "6599301456:AAH9JsrCpd0tckJPxb7Vd0gH39jayQs9urU"


async def echo(message: types.Message):
    print(message.text)
    await message.answer(message.text)


async def start():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.message.register(echo)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start())
