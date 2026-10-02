from aiogram.fsm.state import State, StatesGroup

class DeleteTaskStates(StatesGroup):
    task_id = State()
    ask_confirm = State()
