from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def priority_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="cancel", callback_data="cancel")],
        ],
    )
