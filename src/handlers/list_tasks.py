from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.main_inline import main_keyboard

from database.db import get_tasks

router = Router()

@router.callback_query(F.data == "list_tasks")
async def list_tasks_callback_handler(callback_query: CallbackQuery):
    tasks = await get_tasks(callback_query.from_user.id)
    task_list = "\n".join([f"- {task}" for task in tasks])
    await callback_query.message.answer(f"Here are your tasks:\n{task_list}", reply_markup=main_keyboard(),)
    await callback_query.answer()