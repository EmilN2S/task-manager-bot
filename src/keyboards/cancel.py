from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def cancel_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="cancel", callback_data="cancel")],
        ],
    )
