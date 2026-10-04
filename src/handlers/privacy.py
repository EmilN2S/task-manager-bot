from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.help_inline import help_keyboard

router = Router()

PRIVACY_TEXT = """
Privacy

What we store:
- Your Telegram user ID (to know whose tasks are whose)
- The tasks you create

What we don't do:
- We don't sell or share your data with anyone
- We don't read your other chats or messages

Your data:
- Tasks are stored in src/database/data
- To delete your data, how: Delete task main keyboard
"""

@router.callback_query(F.data == "privacy")
async def privacy_callback_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(PRIVACY_TEXT, reply_markup=help_keyboard())
    await callback_query.answer()
