from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
            [InlineKeyboardButton(text="❓ FAQ", callback_data="faq")],
            [InlineKeyboardButton(text="🔒 Privacy", callback_data="privacy")],
            [InlineKeyboardButton(text="💻 Source Code", callback_data="source_code")],
    )

