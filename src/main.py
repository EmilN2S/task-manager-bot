from os import getenv
from dotenv import load_dotenv
import asyncio

from aiogram import Bot, Dispatcher

from handlers.start import router as start_router
from handlers.help import router as help_router

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(help_router)

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())