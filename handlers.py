import logging

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery


logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):

    await message.answer(text=message.text)


@router.message()
async def send_echo(message: Message):

    await message.answer(text=message.text)
    print(message.model_dump_json(indent=4))


@router.callback_query()
async def callback_answer(callback: CallbackQuery):

    await callback.answer()
    print(callback.model_dump_json(indent=4))
