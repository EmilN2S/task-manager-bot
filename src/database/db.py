import aiosqlite

DB_NAME = "tasks.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT FALSE,
            priority INTEGER DEFAULT 0
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
        cursor = await db.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        return await cursor.fetchall()
        
