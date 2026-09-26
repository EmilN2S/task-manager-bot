from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.inline import main_keyboard

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Hi, {message.from_user.first_name}!", reply_markup=main_keyboard())