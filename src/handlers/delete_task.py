from aiogram import Router, F
from aiogram.types import CallbackQuery, Message   
from aiogram.fsm.context import FSMContext

from keyboards.delete import delete_keyboard

from states.delete_task import DeleteTaskStates

from database.db import get_tasks_lite, delete_task

router = Router()

@router.callback_query(F.data == "delete_task")
async def list_tasks_callback_handler(callback_query: CallbackQuery):
    tasks = await get_tasks_lite(callback_query.from_user.id)
    if not tasks:
        await callback_query.message.answer("You have no tasks.")
        await callback_query.answer()
        return
    task_list = "\n".join([f"- {task}" for task in tasks])
    await callback_query.message.answer(f"Here are your tasks:\n{task_list}\nEnter the task ID you want to delete")
    await callback_query.answer()

@router.message(DeleteTaskStates.task_id, F.text)
async def process_task_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Please enter a valid task ID (a number).")
        return
    await state.update_data(task_id=int(message.text))
    await message.answer(f"Are you sure you want to delete the task?", reply_markup=delete_keyboard())
    await state.set_state(DeleteTaskStates.ask_confirm)

@router.callback_query(DeleteTaskStates.ask_confirm, F.data == "confirm_delete")
async def process_task_delete(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    task_id = data['task_id']
    delete_result = await delete_task(user_id=callback.from_user.id, id=task_id)
    await state.clear()
    await callback.message.answer(f"✅ Task ID: <b>{task_id}</b> has been deleted.", parse_mode="HTML")
    await callback.answer()