import datetime
import asyncpg

pool = None

async def init_db(url):
    global pool

    pool = await asyncpg.create_pool(url)

    await pool.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            user_id BIGINT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            task_status BOOLEAN DEFAULT FALSE,
            priority BOOLEAN DEFAULT FALSE,
            deadline DATE
        )
    ''')

async def close_db():
    await pool.close()

async def add_tasks(user_id, title, description, priority, deadline):
    if isinstance(deadline, str):
        deadline = datetime.date.fromisoformat(deadline)

    await pool.execute('''
        INSERT INTO tasks(user_id, title, description, priority, deadline)
        VALUES($1, $2, $3, $4, $5)
    ''', user_id, title, description, priority, deadline)