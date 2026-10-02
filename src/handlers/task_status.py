from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.status import status_keyboard

from states.priority_status import PriorityStates

from database.db import change_task_status, get_tasks_lite

router = Router()

@router.callback_query(F.data == "task_status")
async def list_tasks_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    tasks = await get_tasks_lite(callback_query.from_user.id)
    if not tasks:
        await callback_query.message.answer("You have no tasks to change the status for.")
        await callback_query.answer()
        return
    task_list = "\n".join([f"- {task}" for task in tasks])
    await callback_query.message.answer(f"Here are your tasks:\n{task_list}\nPlease enter the ID of the task you want to change the status for.")
    await state.set_state(PriorityStates.task_id)


@router.message(PriorityStates.task_id, F.text)
async def process_task_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Please enter a valid task ID (a number).")
        return
    await state.update_data(task_id=int(message.text))
    await message.answer("Choose Finish if the task is completed, or Cancel to keep it active.", reply_markup=status_keyboard())
    await state.set_state(PriorityStates.task_status)


@router.callback_query(PriorityStates.task_status, F.data == "finish")
async def process_task_status(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await change_task_status(user_id=callback.from_user.id, id=data['task_id'], completed=True)
    await state.clear()
    await callback.message.answer(f"✅ Task ID: <b>{data['task_id']}</b> status changed to: <b>Finished</b>", parse_mode="HTML")
    await callback.answer()

@router.callback_query(PriorityStates.task_status, F.data == "cancel")
async def process_task_priority(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await callback.message.answer("Changes denied")