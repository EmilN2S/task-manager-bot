from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.create_task_states import TaskStates

from keyboards.priority import priority_keyboard
from keyboards.cancel import cancel_keyboard
from keyboards.deadline import deadline_keyboard

from database.db import add_task

router = Router()

@router.callback_query(F.data == "cancel")
async def cancel_callback(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text("Creating task canceled")
    await callback.answer()

async def save_task(user_id: int, state: FSMContext, deadline: str | None) -> None:
    data = await state.get_data()
    await add_task(
        user_id=user_id,
        title=data["task_name"],
        description=data["task_description"],
        priority=0 if data["task_priority"] == "simple" else 1,
        deadline=deadline,
    )
    await state.clear()

@router.callback_query(F.data == "add_task")
async def tasks_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Please enter the task name:", reply_markup=cancel_keyboard())
    await state.set_state(TaskStates.task_name)
    await callback.answer()

@router.message(TaskStates.task_name, F.text)
async def process_task_name(message: Message, state: FSMContext):
    await state.update_data(task_name=message.text)
    await message.answer("Please enter the task description:", reply_markup=cancel_keyboard())
    await state.set_state(TaskStates.task_description)

@router.message(TaskStates.task_description, F.text)
async def process_task_description(message: Message, state: FSMContext):
    await state.update_data(task_description=message.text)
    await message.answer("Please enter the task priority:", reply_markup=priority_keyboard())
    await state.set_state(TaskStates.task_priority)

@router.callback_query(TaskStates.task_priority)
async def process_task_priority(callback: CallbackQuery, state: FSMContext):
    await state.update_data(task_priority=callback.data)
    await callback.message.answer(f"Priority set: <b>{callback.data}</b>\n\nPlease enter the task Deadline, you can save task with empty deadline", parse_mode="HTML", reply_markup=deadline_keyboard())
    await state.set_state(TaskStates.task_deadline)
    await callback.answer()

@router.callback_query(TaskStates.task_deadline, F.data == "skip_deadline")
async def skip_deadline(callback: CallbackQuery, state: FSMContext):
    await save_task(callback.from_user.id, state, deadline=None)
    await callback.message.answer("✅ Task saved without a deadline!")
    await callback.answer()

@router.message(TaskStates.task_deadline, F.text)
async def process_task_deadline(message: Message, state: FSMContext):
    await save_task(message.from_user.id, state, deadline=message.text)
    await message.answer("✅ Task saved successfully!")
