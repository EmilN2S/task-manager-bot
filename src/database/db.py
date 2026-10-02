import aiosqlite
from pathlib import Path

DB_DIR = Path(__file__).parent / "data"
DB_NAME = DB_DIR / "tasks.db"

async def init_db():
    DB_DIR.mkdir(exist_ok=True)
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT FALSE,
            priority BOOLEAN DEFAULT FALSE
        )
        """)
        await db.commit()

async def add_task(user_id, title, description=None, priority=0):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT INTO tasks (user_id, title, description, priority)
        VALUES (?, ?, ?, ?)
        """, (user_id, title, description, priority))
        await db.commit()

async def get_tasks(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT id, title, description, priority, completed FROM tasks WHERE user_id = ?", (user_id,))
        return await cursor.fetchall()

async def get_tasks_lite(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT id, title FROM tasks WHERE user_id = ?", (user_id,))
        return await cursor.fetchall()
        
async def change_task_status(user_id, id, completed):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("UPDATE tasks SET completed = ? WHERE user_id = ? AND id = ?", (completed, user_id, id))
        await db.commit()

async def delete_task(user_id, id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DELETE FROM tasks WHERE user_id = ? AND id = ?", (user_id, id))
        await db.commit()