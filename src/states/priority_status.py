from aiogram.fsm.state import State, StatesGroup

class TaskStates(StatesGroup):
    task_id = State()
