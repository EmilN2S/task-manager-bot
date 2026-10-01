from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.status import status_keyboard

from database.db import change_task_status, get_tasks_lite

router = Router()

@router.callback_query(lambda c: c.data == "task_status")
async def list_tasks_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    tasks = await get_tasks_lite(callback_query.from_user.id)
    task_list = "\n".join([f"- {task}" for task in tasks])
    await callback_query.message.answer(f"Here are your tasks:\n{task_list}\nPlease enter the ID of the task you want to change the status for", reply_markup=status_keyboard(),)
    await callback_query.answer()

@router.message(F.text)
async def process_task_id(message: Message, state: FSMContext):
    await state.update_data(task_id=message.text)

