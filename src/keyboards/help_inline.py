from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="❓ FAQ", callback_data="faq")],
            [InlineKeyboardButton(text="🔒 Privacy", callback_data="privacy")],
            [InlineKeyboardButton(text="💻 Source Code", url="https://github.com/EmilN2S/task-manager-bot")],
        ]
    )

