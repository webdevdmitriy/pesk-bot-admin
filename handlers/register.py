from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.database import Database


async def start_register(message: Message, state: FSMContext):
    db = Database(os.getenv("DATABASE_NAME"))
    users = db.select_user_id(message.from_user.id)
    if users:
        await message.answer(f"{users[1]} \n Вы уже зарегистрированы")
    else:
        await message.answer(f"Давайте начнем регистрацию.\n Укажите ваше ФИО?")
        await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f"Теперь укажите ваш номер кабинета")
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.сabinetNumber)


async def register_сabinetNumber(message, state: FSMContext):
    await state.update_data(сabinetNumber=message.text)
    reg_data = await state.get_data()
    reg_name = reg_data.get("regname")
    reg_сabinetNumber = reg_data.get("сabinetNumber")
    msg = f"{reg_name}, вы успшно зарегстрированы. \n Номер вашего кабинета: {reg_сabinetNumber}"
    await message.answer(msg)
    db = Database(os.getenv("DATABASE_NAME"))
    db.add_user(reg_name, reg_сabinetNumber, message.from_user.id)
    await state.clear()
