from aiogram import Bot
from aiogram.types import BotCommand, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def set_main_menu(bot: Bot, commands: dict) -> None:
    bot_commands = [
        BotCommand(command=command, description=description)
        for command, description in commands.items()
    ]
    await bot.set_my_commands(bot_commands)


def create_keyboard(*buttons, width: int | None = None):
    if width is None:
        width = len(buttons)
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        *[InlineKeyboardButton(text=button, callback_data=button)
          for button in buttons],
        width=width
    )
    return kb_builder.as_markup()
