from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Here will be help information. (Coming soon!)")