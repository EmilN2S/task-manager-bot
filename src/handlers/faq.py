from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.help_inline import help_keyboard

router = Router()

FAQ_TEXT = """
Q: What is this bot?
A: A simple Telegram bot for managing your daily tasks.

Q: How do I use it?
A: Just use the buttons under the messages. Everything is controlled with inline buttons, so you don't need to remember any commands.

Q: Can I set deadlines for tasks?
A: Not yet. Deadlines are planned for a future update.

Q: The bot isn't responding. What should I do?
A: Send /start to restart it. If it still doesn't work, the bot may be temporarily offline, so try again a bit later.

Q: I found a bug or have an idea. Where can I tell you?
A: Open an issue on GitHub using the "Source code" button below.

Q: Is the bot open source?
A: Yes, under the MIT license. The code is available via the "Source code" button below.
"""

@router.callback_query(F.data == "faq")
async def help_callback_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(FAQ_TEXT, reply_markup=help_keyboard())
    await callback_query.answer()

