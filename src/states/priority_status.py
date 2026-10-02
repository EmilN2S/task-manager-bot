from aiogram.fsm.state import State, StatesGroup

class PriorityStates(StatesGroup):
    task_id = State()
    task_status = State()
