from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, callback_query

from keyboards.inline import main_keyboard

router = Router()

HELP_TEXT = """
Here will be help information. (Coming soon!)
"""

@router.callback_query(lambda c: c.data == "help")
async def help_callback_handler(callback_query: callback_query):
    await callback_query.message.answer(HELP_TEXT, reply_markup=main_keyboard())

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(HELP_TEXT, reply_markup=main_keyboard())