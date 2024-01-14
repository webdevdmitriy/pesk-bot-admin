from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState


async def start_register(message: Message, state: FSMContext):
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
    await state.clear()
