from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.main_inline import main_keyboard
from database.pgdb import get_tasks
from utils import priority_bool_to_str, completed_bool_to_str

router = Router()

@router.callback_query(F.data == "list_tasks")
async def list_tasks_callback_handler(callback_query: CallbackQuery):
    tasks = await get_tasks(callback_query.from_user.id)

    if not tasks:
        text = "You have no tasks yet"
    else:
        lines = []
        for i, (_, title, description, priority, task_status, deadline) in enumerate(tasks, start=1):
            lines.append(
                f"{i}. {title}\n"
                f"{description or '—'}\n"
                f"Deadline: {deadline or 'none'}\n"
                f"Priority: {priority_bool_to_str(priority)}, "
                f"Completed: {completed_bool_to_str(task_status)}"
            )
        text = "Your tasks:\n\n" + "\n\n".join(lines)

    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.message.answer(text, reply_markup=main_keyboard())
    await callback_query.answer()
