from os import getenv
from dotenv import load_dotenv
import asyncio

from aiogram import Bot, Dispatcher

from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.create_tasks import router as create_tasks_router
from handlers.list_tasks import router as list_tasks_router
from handlers.task_status import router as task_status_router
from handlers.delete_task import router as delete_task_router

from database.db import init_db

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(create_tasks_router)
dp.include_router(list_tasks_router)
dp.include_router(task_status_router)
dp.include_router(delete_task_router)

async def main():
    bot = Bot(token=TOKEN)
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
