from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Help", callback_data="help")],
        ],
        resize_keyboard=True,
    )
    return keyboard