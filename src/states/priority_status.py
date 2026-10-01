from aiogram.fsm.state import State, StatesGroup

class Priority_States(StatesGroup):
    task_id = State()
    task_status = State()
