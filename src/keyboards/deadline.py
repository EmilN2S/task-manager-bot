from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def deadline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Skip", callback_data="skip_deadline")],
        [InlineKeyboardButton(text="Cancel", callback_data="cancel")],
    ])
