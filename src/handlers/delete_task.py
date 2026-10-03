from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards.delete import delete_keyboard
from keyboards.main_inline import main_keyboard

from states.delete_task import DeleteTaskStates
from database.db import get_tasks_lite, delete_task

router = Router()

@router.callback_query(F.data == "delete_task")
async def start_delete(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    tasks = await get_tasks_lite(callback.from_user.id)
    if not tasks:
        await callback.message.answer("You have no tasks.")
        return

    task_list = "\n".join(f"- {task}" for task in tasks)
    await callback.message.answer(
        f"Here are your tasks:\n{task_list}\nEnter the task ID you want to delete"
    )
    await state.set_state(DeleteTaskStates.task_id)

@router.message(DeleteTaskStates.task_id, F.text)
async def process_task_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Please enter a valid task ID (a number).")
        return

    task_id = int(message.text)
    await state.update_data(task_id=task_id)
    await message.answer(
        f"Are you sure you want to delete task {task_id}?",
        reply_markup=delete_keyboard(),
    )
    await state.set_state(DeleteTaskStates.ask_confirm)

@router.callback_query(DeleteTaskStates.ask_confirm, F.data == "confirm_delete")
async def process_task_delete(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    data = await state.get_data()
    task_id = data["task_id"]

    await delete_task(user_id=callback.from_user.id, id=task_id)

    await state.clear()
    await callback.message.answer(
        f"✅ Task ID: <b>{task_id}</b> has been deleted.", parse_mode="HTML"
    )

@router.callback_query(DeleteTaskStates.ask_confirm, F.data == "cancel")
async def process_cancel_delete(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.clear()
    await callback.message.answer("Deleting is denied", reply_markup=main_keyboard())
