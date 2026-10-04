from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.help_inline import help_keyboard

router = Router()

FAQ_TEXT = """

"""

@router.callback_query(F.data == "faq")
async def help_callback_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(FAQ_TEXT, reply_markup=help_keyboard())
    await callback_query.answer()

