from aiogram.fsm.state import State, StatesGroup

class TaskStates(StatesGroup):
    task_name = State()
    task_description = State()
    task_priority = State()