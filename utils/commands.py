from aiogram import Bot
from aiogram.filters import command
from aiogram.types import BotCommand, BotCommandScopeDefault


# Команды для меню
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Зупускаем бота"),
        BotCommand(command="help", description="Помощь в работе с Ботом"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
