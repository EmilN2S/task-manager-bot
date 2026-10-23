from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.help_inline import help_keyboard

router = Router()

HELP_TEXT = """
📖 Help & Support

Need help with the bot?

❓ FAQ — frequently asked questions
🔒 Privacy — information about data storage
💻 Source Code — view the project on GitHub

↩️ To return to the main menu, use /start.
"""

@router.callback_query(F.data == "help")
async def help_callback_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(HELP_TEXT, reply_markup=help_keyboard())
    await callback_query.answer()

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(HELP_TEXT, reply_markup=help_keyboard())
