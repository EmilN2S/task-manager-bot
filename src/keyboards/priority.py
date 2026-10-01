from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def priority_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Simple", callback_data="simple")],
            [InlineKeyboardButton(text="Important", callback_data="important")],
        ],
    )
    return keyboard