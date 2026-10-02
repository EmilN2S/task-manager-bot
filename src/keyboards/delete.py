from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def delete_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Delete", callback_data="confirm_delete")],
            [InlineKeyboardButton(text="Cancel", callback_data="cancel")],
        ],
    )
    return keyboard