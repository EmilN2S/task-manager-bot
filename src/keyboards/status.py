from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def status_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Finish", callback_data="finish")],
            [InlineKeyboardButton(text="Cancel", callback_data="cancel")],
        ],
    )
    return keyboard