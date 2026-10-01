from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def priority_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Finish", callback_data="finish")],
            [InlineKeyboardButton(text="Cancel", callback_data="cancel")],
        ],
        resize_keyboard=True,
    )
    return keyboard