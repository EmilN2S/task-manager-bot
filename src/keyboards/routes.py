from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Add Task", callback_data="add_task")],
            [InlineKeyboardButton(text="🗑️ Delete Task", callback_data="delete_task")],
            [InlineKeyboardButton(text="📋 List Tasks", callback_data="list_tasks")],
            [InlineKeyboardButton(text="📊 Change Task Status", callback_data="task_status")],
            [InlineKeyboardButton(text="❓ Help", callback_data="help")],
        ],
        resize_keyboard=True,
    )
    return keyboard